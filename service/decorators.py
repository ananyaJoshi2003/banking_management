from colorama import Fore, Style, init

from view.login import check
    # use check here


# is_logged_in = False  # Global variable to track login state

# def login_required(func):
#     def inner(account_no):
#         if check== False:
#             print(f"{Fore.RED}You must be logged in to perform this action. Please log in first.{Style.RESET_ALL}")
#             return
#         else:
#             print("chl rha h sb")
            
#         return func(account_no)
#     return inner

def login_required(func):
    auth= check()
    def inner(*args, **kwargs):

        if auth== False:
            print(f"{Fore.RED}You must be logged in to perform this action. Please log in first.{Style.RESET_ALL}")
            return
        # else:
        #     print("chl rha h sb")
        return func(*args, **kwargs)
    return inner
