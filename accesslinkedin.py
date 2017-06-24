# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import linkedin
import requests
import oauth2 as oauth
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

os.chdir('repos/keepint')
# Load LinkedIn credentials
load_dotenv('.env')

KEY = os.environ.get('CLIENT_ID')
SECRET = os.environ.get('CLIENT_SECRET')

URI = 'http%3A%2F%2Fwww.honda.com.br'

AUTH_URL = 'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=' + \
KEY + '&redirect_uri=' + URI + '&state=987654321&scope=r_basicprofile'

# Code originally from URI 
CODE = os.environ.get('ACCESS_CODE')

URL = 'https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code=' + CODE + \
'&redirect_uri=' + URI + '&client_id=' + KEY + '&client_secret=' + SECRET

# Token originally from LinkedIn JSON
TOKEN = os.environ.get('ACCESS_TOKEN')

