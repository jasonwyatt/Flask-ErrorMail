Flask-ErrorMail
======================================

.. module:: Flask-ErrorMail

It is often difficult to quickly debug 500 errors that occur on your Flask application, especially if you are not the one to cause the error.  

The **Flask-ErrorMail** extension provides a simple tool for configuring your `Flask`_ application to automatically send stacktrace emails to a list of administrators whenever an Internal Server Error happens. 

Source code and issue tracking at `Github`_.

Windows issues
--------------

**Flask-ErrorMail** requires Flask-`Mail`_ which in turn, requires the use of 
the **Lamson** library, which unfortunately has dependencies that do not work on 
Windows.

You can install Flask-ErrorMail, Lamson and other libraries with the 
`no dependencies` option::

    easy_install -N lamson chardet Flask-ErrorMail


Installing Flask-ErrorMail
--------------------------

Install with **pip** and **easy_install**::

    pip install Flask-ErrorMail

or download the latest version from Github::

    git clone https://github.com/jasonwyatt/Flask-ErrorMail.git

    cd Flask-ErrorMail

    python setup.py install

If you are using **virtualenv**, it is assumed that you are installing flask-mail
in the same virtualenv as your Flask application(s).

Configuring Flask-ErrorMail
---------------------------

**Flask-ErrorMail** depends on **Flask-Mail**, which is configured through the 
standard Flask config API. You can see those configuration options at the 
Flask-`Mail`_ docs.

Configuration of **Flask-ErrorMail** is done via the *mail_on_500* function::

    from flask import Flask
    from flask_errormail import mail_on_500

    ADMINISTRATORS = (
        # e-mail addresses
    )

    app = Flask(__name__)
    mail_on_500(app, ADMINISTRATORS)

API
---
.. autofunction:: flask_errormail.mail_on_500

.. _Flask: http://flask.pocoo.org
.. _Github: http://github.com/jasonwyatt/Flask-ErrorMail
.. _Mail: http://packages.python.org/flask-mail/