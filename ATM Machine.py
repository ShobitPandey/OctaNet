balance = 6000
pin = '171025'
transactions = []

while True:
    print("\n1. Check Balance")
    print("2. Cash Deposit")
    print("3. Cash Withdraw")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        transactions.append('Checked balance')
        print(f'Current balance: {balance}')

    elif choice == '2':
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        transactions.append(f'Deposited {amount}')
        print(f'{amount} deposited successfully.')

    elif choice == '3':
        input_pin = input("Enter PIN: ")
        if input_pin == pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                transactions.append(f'Withdrew {amount}')
                print(f'{amount} withdrawn successfully.')
            else:
                print('Insufficient balance.')
        else:
            print('Incorrect PIN.')

    elif choice == '4':
        old_pin = input("Enter old PIN: ")
        if old_pin == pin:
            new_pin = input("Enter new PIN: ")
            pin = new_pin
            transactions.append('PIN changed')
            print("PIN successfully changed.")
        else:
            print("Incorrect old PIN.")

    elif choice == '5':
        print('Transaction history:')
        for transaction in transactions:
            print(transaction)

    elif choice == '6':
        print("Have a Good Day!")
        break
    else:
        print("Invalid choice. Please try again.")
