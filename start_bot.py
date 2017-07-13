# import requests,urllib
# from constants import APP_ACESS_TOKEN,BASE_URL
# from colorama import Fore,Back,Style
# from self_info import self_info
# from get_user_info import get_user_info
# from get_own_post import get_own_post
# from get_user_id import get_user_id
# from get_users_post import get_users_post
# from like_user_post import like_a_post
# from get_post_comment import post_a_comment
# from del_negative_comments import delete_negative_comment
# # from termcolor import colored
# def start_bot():
#     while True:
#         print '\n'
#         print (Fore.RED + 'Hey! Welcome to instaBot! \n')
#         print (Back.LIGHTCYAN_EX + 'Here are your menu options.please choose any one of the option:')
#         print (Fore.RED +"1.Get your self details\n")
#         print "2.Get details of a user \n"
#         print "3.Get your own recent post\n"
#         print "4.Get user id\n"
#         print "5.Get the recent post of a user\n"
#         print "6.Like the recent post of a user\n"
#         print "7.Make a comment on the recent post of a user\n"
#         print "8.Delete negative comments from the recent post of a user\n"
#         print "9.Exit"
#
#         choice = raw_input(Fore.GREEN+ "Enter you choice: ")
#         if choice == "1":
#             self_info()
#         elif choice == "2":
#             instagram_username = raw_input(Back.LIGHTCYAN_EX+Fore.RED +"Enter the username of the user: ")
#             get_user_info(instagram_username)
#         elif choice == "3":
#             instagram_username = raw_input(Back.LIGHTCYAN_EX + Fore.RED + "Enter the username of the user: ")
#             get_own_post()
#         elif choice == "4":
#             instagram_username = (raw_input(Back.LIGHTCYAN_EX + Fore.RED + "Enter the username of the user: "))
#             get_user_id()
#         elif choice == "5":
#             instagram_username = (raw_input(Back.LIGHTCYAN_EX + Fore.RED +"Enter the username of the user: "))
#             get_users_post(instagram_username)
#         elif choice=="6":
#             instagram_username = (raw_input(Back.LIGHTCYAN_EX + Fore.RED +"Enter the username of the user: "))
#             like_a_post(instagram_username)
#         elif choice=="7":
#             instagram_username = (raw_input(Back.LIGHTCYAN_EX + Fore.RED +"Enter the username of the user: "))
#             post_a_comment(instagram_username)
#         elif choice=="8":
#             instagram_username = (raw_input(Back.LIGHTCYAN_EX + Fore.RED +"Enter the username of the user: "))
#             delete_negative_comment(instagram_username)
#         elif choice == "9":
#             exit()
#         else:
#             print "wrong choice"
# start_bot()