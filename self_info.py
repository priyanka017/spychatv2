#self info functions
import requests
from constants import APP_ACESS_TOKEN ,BASE_URL


def self_info():
    #function logic
    request_url = (BASE_URL + 'users/self/?4151591513.f66ea55.13515bcb8e1245a5bbca70ca778e55c4=%s') % ('4151591513.f66ea55.13515bcb8e1245a5bbca70ca778e55c4')
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'