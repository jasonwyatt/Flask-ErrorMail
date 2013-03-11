import unittest
import mailbox

from flask import Flask
from flask_errormail import mail_on_500

from nose.tools import assert_equal

def test_install_sanity():
    mail_on_500(Flask('Fake Flask App'), ('foo@example.com',))
