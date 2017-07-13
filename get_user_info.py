#fetches user info from instagram
# from get_user_id import get_user_id
import requests
from constants import APP_ACESS_TOKEN,BASE_URL


def get_user_info(instagram_username):
    #function logic
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (instagram_username,APP_ACESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    print user_info
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data'][0]['username'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'
        exit()
#get_user_info('yogesh_biebz')




