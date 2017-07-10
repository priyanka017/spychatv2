#instabot.py file initialized
import requests
import urllib
from textblob import TextBlob
from constants import APP_ACESS_TOKEN,BASE_URL

start_bot()

#fetching own recent data
result =get_own_post()
print result

