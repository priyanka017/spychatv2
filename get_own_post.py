import requests
import urllib
from constants import APP_ACESS_TOKEN,BASE_URL
def get_own_post():
    #functions logic
    request_url = (BASE_URL + 'users/self/media/recent/?=4151591513.f66ea55.13515bcb8e1245a5bbca70ca778e55c4%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        # extract post ID
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'