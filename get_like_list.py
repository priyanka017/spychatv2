import requests
from constants import APP_ACESS_TOKEN,BASE_URL
from get_post_id import get_post_id

#insta_username= "yogesh_biebz"

def like_list(insta_username):
  # Overall logic of this function
  media_id = get_post_id(insta_username)

  request_url = (BASE_URL +'media/%s/likes?access_token=%s') % (media_id,APP_ACESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  get_a_like = requests.get(request_url).json()
  print get_a_like
  if get_a_like['meta']['code'] == 200:

    print"Media with media id '{}' is liked by following users:" . format(media_id)
    for (index,user_likes) in enumerate(get_a_like['data']):
        print"{}. {} ({}) - {}".format(index+1,user_likes['full_name'],user_likes['id'],user_likes['username'])
  else:
    print("There is no Like regarding this post.")
#like_list(insta_username)