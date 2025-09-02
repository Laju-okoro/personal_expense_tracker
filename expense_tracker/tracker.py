import os
from datetime import datetime
from collections import defaultdict
from colorama import Fore, Style, init

# Initializing colorama
init(autoreset=True)

# CONFIG

FILE_NAME = 'expenses.txt'
CURRENCY = '$'

# CORE FUNCTIONS

def format_currency(amount):
    '''Format numbers as currency e.g $5,500.10'''
    return f'{CURRENCY}{amount:,.2f}'

def add_expense():
    '''Add a new expense with validation'''
    try:
        amount = float(input(Fore.CYAN + 'ENTER AMOUNT:'))
    except ValueError:
        print(Fore.RED + '❌ INVALID AMOUNT. PLEASE ENTER A NEW NUMBER.')
        return
    
    category = input(Fore.CYAN + 'ENTER CATEGORY (E.G., FOOD, TRANSPORT):').title()
    description = input(Fore.CYAN + 'ENTER DESCRIPTION:')

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f'{timestamp}|{category}|{amount:.2f}|{description}\n'

    with open(FILE_NAME, 'a') as file:
        file.write(entry)

    print(Fore.GREEN + '✅ EXPENSE ADDED SUCCESSFULLY!')

def view_all_expenses():
    '''Display all expenses neatly in tabular format'''
    if not os.path.exists(FILE_NAME):
        print(Fore.YELLOW + '⚠ NO EXPENSES RECORDED YET!')
        return
    
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

    if not lines:
        print(Fore.YELLOW + '⚠ NO EXPENSES FOUND!')
        return
    
    print(Fore.MAGENTA + '\n--- ALL EXPENSES ---')
    print(f'{Fore.BLUE}{'#':<3} {'Date & Time':<20} {'Category':<12} {'Amount':<12} {'Description'}')
    print(Style.DIM + '-' * 75)

    for idx, line in enumerate(lines, start=1):
        date, category, amount, desc = line.strip().split('|')
        print(f'{Fore.WHITE}{idx:<3} {date:<20} {category:<12} {format_currency(float(amount)):<12} {desc}')

def view_summary_by_category():
    '''Summarize total expenses by category'''
    if not os.path.exists(FILE_NAME):
        print(Fore.YELLOW + '⚠ NO EXPENSES RECORDED YET!')
        return
    
    category_totals = defaultdict(float)

    with open(FILE_NAME, 'r') as file:
        for line in file:
            _, category, amount, _ = line.strip().split('|')
            category_totals[category] += float(amount)

    if not category_totals:
        print(Fore.YELLOW + '⚠ NO EXPENSES FOUND!')
        return
    
    print(Fore.MAGENTA + '\n--- EXPENSE SUMMARY BY CATEGORY ---')
    for cat, total in category_totals.items():
        print(f'{Fore.CYAN}{cat:<12} : {Fore.GREEN}{format_currency(total)}')

def search_by_category():
    '''Search for all expenses in a chosen category'''
    if not os.path.exists(FILE_NAME):
        print(Fore.YELLOW + '⚠ NO EXPENSES RECORDED YET!')
        return
    
    category = input(Fore.CYAN + 'ENTER CATEGORY TO SEARCH:').title()

    with open(FILE_NAME, 'r') as file:
        lines = [line.strip().split('|') for line in file]

    matches = [line for line in lines if line[1] == category]

    if not matches:
        print(Fore.RED + f"⚠️ NO EXPENSES FOUND IN CATEGORY '{category}'.")
        return
    
    print(Fore.MAGENTA + f'\n--- EXPENSES IN {category} ---')
    for idx, (date, cat, amount, desc) in enumerate(matches, start=1):
        print(f'{Fore.WHITE}{idx}. {date} | {cat} | {format_currency(float(amount))} | {desc}')

def delete_expense():
    '''Delete an expense by its number'''
    if not os.path.exists(FILE_NAME):
        print(Fore.YELLOW + '⚠ NO EXPENSES RECORDED YET!')
        return
    
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

    if not lines:
        print(Fore.YELLOW + 'NO EXPENSES TO DELETE!')
        return
    
    view_all_expenses()
    try:
        choice = int(input(Fore.CYAN + 'ENTER THE EXPENSE NUMBER TO DELETE:'))
        if 1 <= choice <= len(lines):
            removed = lines.pop(choice - 1)
            with open(FILE_NAME, 'w') as file:
                file.writelines(lines)
            print(Fore.GREEN + f'✅ DELETED {removed.strip()}')
        else:
            print(Fore.RED + '❌ INVALID CHOICE!')

    except ValueError:
        print(Fore.RED + '❌ PLEASE ENTER A VALID NUMBER!')


# MAIN MENU

def main():
    while True:
        print(Fore.YELLOW + '\n=== PERSONAL EXPENSE TRACKER ===')
        print(Fore.CYAN + '1. ➕ ADD EXPENSE')
        print(Fore.CYAN + '2. 📋 VIEW ALL EXPENSES')
        print(Fore.CYAN + '3. 📊 VIEW SUMMARY BY CATEGORY')
        print(Fore.CYAN + '4. 🔍 SEARCH EXPENSES BY CATEGORY')
        print(Fore.CYAN + '5. 🗑️ DELETE AN EXPENSE')
        print(Fore.CYAN + '6. ❌ EXIT')

        choice = input(Fore.MAGENTA + 'CHOOSE AN OPTION: ')

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            view_summary_by_category()
        elif choice == '4':
            search_by_category()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print(Fore.GREEN + '👋🏾 GOODBYE! THANKS FOR USING THE TRACKER.')
            break
        else:
            print(Fore.RED + '❌ INVALID CHOICE, TRY AGAIN')

if __name__ == '__main__':
    main()
