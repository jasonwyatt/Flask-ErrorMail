from flask import Flask, g, request, got_request_exception
from flaskext.mail import Mail, Message

_sender = None
_recipients = []
_mail = None

def mail_on_500(app, recipients, sender='noreply@localhost'):
    '''Main function for setting up Flask-ErrorMail to send e-mails when 500 
    errors occur.

    :param app: Flask Application Object
    :type app: flask.Flask
    :param recipients: List of recipient email addresses.
    :type recipients: list or tuple

    '''

    assert isinstance(recipients, list) or isinstance(recipients, tuple)
    assert len(recipients) > 0

    _mail = Mail(app)
    _sender = sender
    _recipients = recipients
    got_request_exception.connect(_email_exception, app)

def _email_exception(sender, exception, **extra):
    '''Handles the exception message from Flask by sending an email to the 
    recipients defined in the call to mail_on_500

    '''

    msg = Message("[Flask|ErrorMail] Exception Detected: %s" % exception.message,
                  sender=g.flask_errormail_sender,
                  recipients=g.flask_errormail_recipients)
    msg.body = '%s\n\n%s' % (traceback.format_exc(), '\n'.join(['%s: %s' % (key, extra[key]) for key in extra]))
    _mail.send(msg)
