import csv
import os
from datetime import datetime
from colorama import init, Fore, Style
from service.retrive_account_details import get_accounts

# def log_transaction(account_no, transaction_type, amount):

#     file_exists = os.path.isfile('transactions.csv')
    
#     with open('transactions.csv', 'a', newline='') as file:
#         writer = csv.writer(file)

#         if not file_exists:
#             writer.writerow(['account_number', 'date', 'type', 'amount'])

#         writer.writerow([account_no, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), transaction_type, amount])

def view_last_transactions(account_no):
    try:
        with open('transaction_history.csv', 'r') as file:
            reader = csv.reader(file)
            print(f"{Fore.YELLOW}=== Transaction History for Account Number: {account_no} ==={Style.RESET_ALL}")
            found = False
            for row in reader:
                if row[1] == account_no:
                    found = True
                    print(f"Date: {row[0]}, Type: {row[2]}, Amount: {row[3]}, New Balance: {row[4]}")
            if not found:
                print(f"{Fore.RED}No transactions found for this account.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Transaction history file not found.{Style.RESET_ALL}")












# all_accounts= get_accounts()

# account_number = '12000'

# log_transaction(account_number, 'Credit', 1000)

# view_last_transactions(account_number)




# import csv
# import os
# from datetime import datetime
# from service.retrive_account_details import get_accounts
# from view.credit import credit_money
# from view.debit import debit_money

# def log_transaction(account_no, transaction_type, amount):
#     file_exists = os.path.isfile('transactions.csv')
    
#     with open('transactions.csv', 'a', newline='') as file:
#         writer = csv.writer(file)

#         if not file_exists:
#             writer.writerow(['account_number', 'date', 'type', 'amount'])

#         writer.writerow([account_no, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), transaction_type, amount])


# def view_last_transactions(account_no, num_transactions=5):
#     print("=== Last Transactions ===")
    
#     transactions = []
    
#     if os.path.isfile('transactions.csv'):
#         with open('transactions.csv', 'r') as file:
#             reader = csv.DictReader(file)

#             for row in reader:
#                 if row['account_number'] == account_no:
#                     transactions.append(row)

#         if not transactions:
#             print("No transactions found for this account.")
#             return
        
#         print(f"Displaying the last {min(num_transactions, len(transactions))} transactions:")
#         for transaction in transactions[-num_transactions:]:
#             print(f"Date: {transaction['date']}, Type: {transaction['type']}, Amount: ${float(transaction['amount']):.2f}")
#     else:
#         print("Transaction history file not found.")