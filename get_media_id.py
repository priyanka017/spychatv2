import requests
from constants import APP_ACESS_TOKEN, BASE_URL

from get_user_id import get_user_id

def get_media_id():
 #FUNCTION LOGIC
    instagram_username = "yogesh_biebz"
    user_id = get_user_id(instagram_username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id,APP_ACESS_TOKEN)
    print 'GET request url :%s' % (request_url)
    user_info = requests.get(request_url).json()
    print user_info
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            print 'There is no recent post of the user'
    else:
         print 'Status code other than 200 received'
