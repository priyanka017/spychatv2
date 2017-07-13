#instabot.py file initialized

#importing libraries
import requests
import urllib

#importing functions
from self_info import self_info
from textblob import TextBlob
from constants import APP_ACESS_TOKEN,BASE_URL
from get_own_post import get_own_post
from menu import *

menu()

#fetching own recent data
result =get_own_post()
print result


