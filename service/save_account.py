# this file is saving my data

# import csv

# def save_account(account_number, account_info):
#     csv_file= 'accounts.csv'
#     file_exists = False

#     try:
#         with open(csv_file, 'r'):
#             file_exists = True
#     except FileNotFoundError:
#         pass

#     with open(csv_file, mode='a', newline='') as file:
#         fieldnames= ['account_number', 'name', 'email', 'password', 'balance']
#         writer= csv.DictWriter(file, fieldnames=fieldnames)

#         if not file_exists:
#             writer.writeheader()

#         account_info['account_number']= account_number
#         writer.writerow(account_info)


import csv
import os
from colorama import init, Fore, Style

def save_account(account_number, account_info):
    csv_file = 'accounts.csv'
    file_exists = os.path.exists(csv_file)

    try:
        with open(csv_file, mode='a', newline='') as file:
            fieldnames = ['account_number', 'name', 'email', 'password', 'balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            account_info['account_number'] = account_number
            writer.writerow(account_info)
    except Exception as e:
        print(f"{Fore.RED}Error saving account: {str(e)}{Style.RESET_ALL}")