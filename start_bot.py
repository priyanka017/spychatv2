from self_info import self_info
from get_user_info import get_user_info
from get_own_post import get_own_post
from get_user_id import get_user_id
from get_users_post import get_users_post
from like_user_post import like_user_post
from get_post_comment import get_post_comment
from del_negative_comments import delete_negative_comment





def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "1.Get your self details\n"
        print "2.Get details of a user \n"
        print "3.Get your own recent post\n"
        print "4.Get user id\n"
        print "5.Get the recent post of a user\n"
        print "6.Like the recent post of a user\n"
        print "7.Make a comment on the recent post of a user\n"
        print "8.Delete negative comments from the recent post of a user\n"
        print "9.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "1":
            self_info()
        elif choice == "2":
            instagram_username = raw_input("Enter the username of the user: ")
            get_user_info(instagram_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            instagram_user_id = raw_input("enter the user id")
            get_user_id()
        elif choice == "5":
            instagram_username = raw_input("Enter the username of the user: ")
            get_users_post(instagram_username)
        elif choice=="6":
           instagram_username = raw_input("Enter the username of the user: ")
           like_user_post(instagram_username)
        elif choice=="7":
           instagram_username = raw_input("Enter the username of the user: ")
           get_post_comment(instagram_username)
        elif choice=="8":
           insta_username = raw_input("Enter the username of the user: ")
           del_negative_comments(instagram_username)
        elif choice == "9":
            exit()
        else:
            print "wrong choice"
