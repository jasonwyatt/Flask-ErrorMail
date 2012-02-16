import unittest
import mailbox

from flask import Flask
from flask_errormail import mail_on_500

from nose.tools import assert_equal
