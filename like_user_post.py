  import requests
  from constants import APP_ACESS_TOKEN,BASE_URL
  from get_users_post import get_users_post

  username = "saloni2408"
  def like_a_post(insta_username):
    post_id =get_user_id(insta_username)
  # print media_id
    request_url = (BASE_URL + '','media/%s/likes') % (post_id)
  payload = {"access_token": APP_ACESS_TOKEN}
  print 'POST request url : %s' % (request_url)
  post_a_like = requests.post(request_url, payload).json()

  if post_a_like['meta']['code'] == 200:
    print "Post Liked Successfully"
  else:
    print "Unable to like post"
like_a_post(username)