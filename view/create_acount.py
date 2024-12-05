# # can use list to velidate and split
# from colorama import init, Fore, Style
# from service.user_valid import *
# from service.save_account import *
# from service.get_account_number import *


# # initializing colorama(for colors in console)
# init()

# def create_account():

#     try:
#         flag= True
#         account_number= get_last_account_number() + 1
#         print(f"{Fore.CYAN}I am here to create your new account!!{Style.RESET_ALL}")
        
#         while flag:
#             name= input(f"{Fore.YELLOW}Enter your name:- {Style.RESET_ALL}")
#             if(check_name(name)):
#                 break
        
#         while flag:
#             email= input(f"{Fore.YELLOW}Enter your email:- {Style.RESET_ALL}")
#             if(check_mail(email)):
#                 break
        
#         while flag:
#             password= input(f'''{Fore.YELLOW}
#             Create password(should have at least 1 number, 1 uppercase, 1 lowercase): 
#             {Style.RESET_ALL}''')

#             if(check_password(password)):
#                 break
        
#         print(f"{Fore.GREEN}----------\nAccount created successfully!!\n----------{Style.RESET_ALL}")
#         print(f'''{Fore.CYAN}
#             Your account no. is{Style.RESET_ALL}", 
#             f"{Fore.WHITE}{account_number}{Style.RESET_ALL}''')
        
#         account_data= {
#             "name": name,
#             "email": email,
#             "password": password,
#         }

#         print(f"{Fore.MAGENTA}Account Details:{Style.RESET_ALL}")

#         for key, value in account_data.items():
#             print(f"{Fore.CYAN}{key}: {Fore.WHITE}{value}{Style.RESET_ALL}")
        
#         save_account(account_number, account_data)
    
#     except Exception as e:
#         print(f"{Fore.RED}Error creating account: {str(e)}{Style.RESET_ALL}")



from colorama import init, Fore, Style
from service.user_valid import *
from service.save_account import *
from service.get_account_number import *

# initializing colorama(for colors in console)
init()

def create_account():
    try:
        flag = True
        account_number = get_last_account_number() + 1
        print(f"{Fore.CYAN}I am here to create your new account!!{Style.RESET_ALL}")
        
        while flag:
            name = input(f"{Fore.YELLOW}Enter your name:- {Style.RESET_ALL}")
            if(check_name(name)):
                break
        
        while flag:
            email = input(f"{Fore.YELLOW}Enter your email:- {Style.RESET_ALL}")
            if(check_mail(email)):
                break
        
        while flag:
            password = input(f'''{Fore.YELLOW}Create password(should have at least 1 number, 1 uppercase, 1 lowercase): 
            {Style.RESET_ALL}''')
            if(check_password(password)):
                break

        while flag:
            initial_balance = input(f"{Fore.YELLOW}Enter initial balance (min ₹500):- {Style.RESET_ALL}")
            if(check_balance(initial_balance)):
                initial_balance = float(initial_balance)
                break
        
        print(f"{Fore.GREEN}----------\nAccount created successfully!!\n----------{Style.RESET_ALL}")
        print(f'''{Fore.CYAN}
            Your account no. is{Style.RESET_ALL}", 
            f"{Fore.WHITE}{account_number}{Style.RESET_ALL}''')
        
        account_data = {
            "name": name,
            "email": email,
            "password": password,
            "balance": initial_balance
        }

        print(f"{Fore.MAGENTA}Account Details:{Style.RESET_ALL}")

        for key, value in account_data.items():
            print(f"{Fore.CYAN}{key}: {Fore.WHITE}{value}{Style.RESET_ALL}")
        
        save_account(account_number, account_data)
    
    except Exception as e:
        print(f"{Fore.RED}Error creating account: {str(e)}{Style.RESET_ALL}")
