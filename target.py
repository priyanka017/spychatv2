import requests
import urllib
from constants import APP_ACESS_TOKEN,BASE_URL
from get_user_id import get_user_id
from get_post_comment import *

def target_a_comment(insta_username)
    user_id = get_user_id(insta_username)
    payload = {"access_token":APP_ACESS_TOKEN}
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id,APP_ACESS_TOKEN)

    print 'GET request url : %s' % (request_url)
    user_media = requests.post(request_url, payload).json()

    if user_media =='coffee':
        print"come at ccd:
    else:
        print"error"
target_a_comment(insta_username='sharmatanu9878')