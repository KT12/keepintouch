# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Credentials stored in .env file in same folder


import linkedin
import requests
import oauth2 as oauth
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
from xml.etree import ElementTree
import xmltodict
import json
from pandas.io.json import json_normalize

print('Rember to use the correct directory for your machine')

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

XML_URL = "https://api.linkedin.com/v1/people/~:(id,first-name,last-name,headline,picture-url,industry,summary,specialties,positions:(id,title,summary,start-date,end-date,is-current,company:(id,name,type,size,industry,ticker)),educations:(id,school-name,field-of-study,start-date,end-date,degree,activities,notes),associations,interests,num-recommenders,date-of-birth,publications:(id,title,publisher:(name),authors:(id,name),date,url,summary),patents:(id,title,summary,number,status:(id,name),office:(name),inventors:(id,name),date,url),languages:(id,language:(name),proficiency:(level,name)),skills:(id,skill:(name)),certifications:(id,name,authority:(name),number,start-date,end-date),courses:(id,name,number),recommendations-received:(id,recommendation-type,recommendation-text,recommender),honors-awards,three-current-positions,three-past-positions,volunteer)?oauth2_access_token=" + TOKEN

XML_response = requests.get(XML_URL)
tree = ElementTree.fromstring(XML_response.content)

XML_data = xmltodict.parse(XML_response.content)

person_df = json_normalize(XML_data).T # Transpose dataframe

idx = person_df.index.values

