"""
    flask_errormail
    ~~~~~~~~~~~~~~~

    Flask extension for sending emails to administrators when 500 Internal 
    Server Errors occur.

    :copyright: (c) 2012 by Jason Wyatt Feinstein.
    :license: MIT, see LICENSE.txt for more details.
    
"""
import traceback
try:
    # putting in try-catch for now... because it could fail on import when the 
    # package is being inspected.
    from flask import Flask as _Flask
    from flask import request as _request
    from flask import got_request_exception as _got_request_exception
    from flaskext.mail import Mail as _Mail 
    from flaskext.mail import Message as _Message
except ImportError:
    print 'Imports not available..'

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
    :param sender: Email address that should be listed as the sender. Defaults 
        to 'noreply@localhost'
    :type sender: string

    '''
    global _mail, _sender, _recipients

    assert isinstance(recipients, list) or isinstance(recipients, tuple)
    assert len(recipients) > 0

    _mail = _Mail(app)
    _sender = sender
    _recipients = recipients
    _got_request_exception.connect(_email_exception, app)

def _email_exception(sender, exception, **extra):
    '''Handles the exception message from Flask by sending an email to the 
    recipients defined in the call to mail_on_500

    '''
    global _mail, _sender, _recipients

    msg = _Message("[Flask|ErrorMail] Exception Detected: %s" % exception.message,
                  sender=_sender,
                  recipients=_recipients)
    msg_contents = [
        'Traceback:',
        '='*80,
        traceback.format_exc(),
    ]
    msg_contents.append('\n')
    msg_contents.append('Request Information:')
    msg_contents.append('='*80)
    environ = _request.environ
    environkeys = sorted(environ.keys())
    for key in environkeys:
        msg_contents.append('%s: %s' % (key, environ.get(key)))
        
    msg_contents.append('\n')
        
    msg_contents.append('Flask Extras:')
    msg_contents.append('='*80)
    for key in extra:
        msg_contents.append('\t%s: %s' % (key, extra[key]))
    
    msg.body = '\n'.join(msg_contents) + '\n'
    
    _mail.send(msg)


__all__ = ['mail_on_500']