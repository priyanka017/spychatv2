import requests
from get_user_id import get_user_id
from constants import APP_ACESS_TOKEN,BASE_URL

def post_a_comment(insta_username):
    media_id = get_user_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"
