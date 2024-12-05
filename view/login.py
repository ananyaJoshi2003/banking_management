from constant.login_constamt import *
import maskpass
from colorama import Fore, Style
from service.retrive_account_details import get_accounts
from view.credit import credit_money
from view.debit import debit_money
from view.transection import view_last_transactions
from view.transfer import transfer_money


is_logged_in = False

def login_account():

    global is_logged_in  # Declared global

    user_id = input("Enter your id (mail id): ")
    password=maskpass.askpass(Fore.MAGENTA +"Enter your password: "+Style.RESET_ALL,mask="*") 
    # password = input("Enter password: ")

    all_accounts = get_accounts()
    login_successful = False

    for account in all_accounts:

        if account['email'] == user_id and account['password'] == password:

            is_logged_in = True

            print("----------------------\nLogin Successful!\n----------------------")
            print("Account Details:")
            print(f"Account Number: {account['account_number']}")
            print(f"Name: {account['name']}")
            print(f"Email: {account['email']}")
            print(f"Current Balance: {account['balance']}")
            print("------------------------------")
            login_successful = True

            while True:
                
                print(f"\n{Fore.GREEN}Menu options:")
                menu = f"""Choose an option:- 
                {Fore.CYAN}1) Credit Money
                {Fore.CYAN}2) Debit Money 
                {Fore.CYAN}3) Transaction history 
                {Fore.CYAN}4) Transfer money
                {Fore.RED}5) Exit {Style.RESET_ALL}
                """
                chose = int(input(menu))
                account_no = account['account_number']

                if chose == CREDIT:
                    print(f"{Fore.YELLOW}=== Credit Money ==={Style.RESET_ALL}")
                    credit_money(account_no)

                elif chose == DEBIT:
                    print(f"{Fore.YELLOW}=== Debit Money ==={Style.RESET_ALL}")
                    debit_money(account_no)

                elif chose == HISTORY:
                    print(f"{Fore.YELLOW}=== Transaction History ==={Style.RESET_ALL}")
                    view_last_transactions(account_no)

                elif chose == TRANSFER:
                    print(f"{Fore.YELLOW}=== Transfer Money ==={Style.RESET_ALL}")
                    to_account_no = input("Enter the account number to transfer to: ")
                    amount = float(input("Enter the amount to transfer: "))
                    transfer_money(account_no, to_account_no, amount)

                elif chose == EXIT:
                    print(f"{Fore.YELLOW}THANK YOU ")
                    break

                else:
                    print(f"{Fore.RED}Invalid option! Please choose a correct option (1-5){Style.RESET_ALL}")

            break
        # return is_logged_in

    if not login_successful:
        print("""----------------------
              Invalid email or password. Please try again.
              ----------------------""")

def check():
    return is_logged_in

# login_account()
# print(check)