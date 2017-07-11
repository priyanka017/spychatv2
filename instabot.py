#instabot.py file initialized
import requests
import urllib

from self_info import self_info
from textblob import TextBlob
from constants import APP_ACESS_TOKEN,BASE_URL
from get_own_post import get_own_post
from start_bot import start_bot
start_bot()

#fetching own recent data
result =get_own_post()
print result


