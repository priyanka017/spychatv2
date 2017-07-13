import requests
from constants import APP_ACESS_TOKEN, BASE_URL
from get_user_info import get_user_info
from get_post_comment import *
from del_negative_comments import *
from like_user_post import like_a_post
from get_user_id import get_user_id
from get_own_post import get_own_post
from self_info import self_info
from get_users_post import get_users_post
from get_media_id import get_media_id
from colorama import Fore,Back,Style
spy_name = "PRIYANKA"
spy_salutation= "Ms."
spy_name =  spy_salutation + " "+ spy_name
def start_insta():
    print " Welcome!.. " + spy_name + " You are connected with instabot!"

    show_menu = True

    while show_menu:
        print('BELOW MENTION YOUR OPTION.PLEASE CHOOSE ANY ONE OF THE OPTION:->\n')
        print (Back.LIGHTCYAN_EX + 'HEY PRIYANKA ! WELCOME TO INSTABOT! \n')
        print (Back.LIGHTCYAN_EX + 'HERE ARE YOUR MENU OPTIONS.PLEASE CHOOSE ANY ONE OF THE OPTION:''\n')
        print (Fore. RED + "1.Get your self details\n")
        print (Fore.RED + "2.Get details of a user \n")
        print (Fore.RED+ "3.Get your own recent post\n")
        print (Fore.RED + "4.Get user id\n")
        print (Fore.RED + "5.Get the recent post of a user\n")
        print (Fore.RED + "6.Like the recent post of a user\n")
        print "7.Make a comment on the recent post of a user\n"
        print "8.Delete negative comments from the recent post of a user\n"
        print "9.Exit"

        instagram_username="yogesh_biebz"
        menu_choice = raw_input(Fore.GREEN+"what do you want to acess.please choose any number")

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)
            if menu_choice == 1:
                self_info()
            elif menu_choice == 2:
                get_user_info(instagram_username)
            elif menu_choice == 3:
                get_own_post()
            elif menu_choice == 4:
                get_user_id(instagram_username)
            elif menu_choice == 5:
                get_users_post(instagram_username)
            elif menu_choice == 6:
                like_a_post()
            elif menu_choice == 7:
                post_a_comment(instagram_username)
            elif menu_choice == 8:
                delete_negative_comment(instagram_username)
            else:
                print "Please enter  one of the option from above........?"

start_insta()