import requests,urllib
from get_user_id import get_user_id
from constants import APP_ACESS_TOKEN ,BASE_URL
from get_users_post import get_users_post

 #function logic
    def get_users_post(insta_username):
        user_id = get_user_id(insta_username)
        if user_id == None:
            print 'User does not exists'
            exit()

        request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id,APP_ACESS_TOKEN)
        print 'GET request url for user post : %s' % (request_url)
        user_media = requests.get(request_url).json()

        if user_media['meta']['code'] == 200:
            # extract post ID
            if len(user_media['data']):
                image_name = user_media['data'][0]['id'] + '.jpeg'
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                return user_media['data'][0]['id']
            else:
                print "There is no recent post!"
        else:
            print 'Status code other than 200 received!'



