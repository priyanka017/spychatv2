import requests,urllib
from constants import BASE_URL,APP_ACESS_TOKEN
from get_post_id import get_post_id

#insta_username= "yogesh_biebz"
def get_comment_list(insta_username):
    # Overall logic of this function
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id,APP_ACESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code'] == 200:
        # if there is some data or info in the comment box.
        if len(comment_info['data']):

            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                print 'Comments are : %s\n' % (comment_text)

        else:
            print("There is no comments regarding this post.")

    else:
        print'Status code other than 200.'
#get_comment_list(insta_username)