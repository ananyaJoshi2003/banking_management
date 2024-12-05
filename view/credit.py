import csv
from colorama import Fore, Style, init

# from service.decorators import login_required

from service.retrive_account_details import get_accounts
from view.log_transaction import log_transaction


# @login_required
def credit_money(account_no):
    
    print(f"{Fore.YELLOW}=== Credit Money ==={Style.RESET_ALL}")
    print(f"Your account number is: {account_no}")

    # is_logged_in = login_account()
    
    amount = input(f"{Fore.CYAN}How much money would you like to credit to your account? {Style.RESET_ALL}")

    if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
        amount = float(amount)

        accounts = get_accounts()
        account_found = False

        for account in accounts:
            if account['account_number'] == account_no:
                account_found = True
                current_balance = float(account['balance'])
                new_balance = current_balance + amount
                account['balance'] = new_balance  

                print(f"{Fore.GREEN}Successfully credited {amount} to your account! New balance: {new_balance}{Style.RESET_ALL}")

                # Log the transaction
                log_transaction(account_no, 'credit', amount, new_balance)

                break

        if account_found:
            with open('accounts.csv', 'w', newline='') as file:
                fieldnames = ['account_number', 'name', 'email', 'password', 'balance']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(accounts)
        else:
            print(f"{Fore.RED}Account not found.{Style.RESET_ALL}")

    else:
        print(f"{Fore.RED}Invalid input! Please enter a valid amount greater than zero.{Style.RESET_ALL}")
