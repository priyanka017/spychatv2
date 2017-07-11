import requests
import urllib
from constants import APP_ACESS_TOKEN,BASE_URL
from get_user_id import get_user_id

from get_post_comment import *


def target_a_comment(insta_username):
  user_id = get_user_id(insta_username)

  request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id,APP_ACESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_media = requests.get(request_url).json()

  service = [ 'clothes','shoes','Pizza..','coffee','Ice-cream']
  for post in user_media['data']:
      for serve in service:
          if serve in post['caption']['text']:
            post_a_comment(insta_username)
          else:
              print'Not match by user\'s interst'

