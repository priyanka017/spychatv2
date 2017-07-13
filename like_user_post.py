import requests
import urllib
from constants import APP_ACESS_TOKEN,BASE_URL
# from get_users_post import get_users_post
from get_user_id import get_user_id
from get_media_id import get_media_id

# instagram_username = "yogesh_biebz"

def like_a_post():
    # Overall logic of this function
    media_id =get_media_id()
    # print media_id
    request_url = (BASE_URL +'media/%s/likes') % (media_id)
    print request_url
    payload = {"access_token": APP_ACESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()

    if post_a_like['meta']['code'] == 200:
        print "Post Liked Successfully"
    else:
        print ("Unable to like post")

#like_a_post()