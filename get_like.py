import requests
import urllib
from constants import BASE_URL,APP_ACESS_TOKEN
from get_users_post import get_users_post
from get_post_id import get_post_id

user = 'yogesh_biebz'
def like_a_post(instagram_username):
    # Overall logic of this function
    media_id =get_post_id(instagram_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token":APP_ACESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

