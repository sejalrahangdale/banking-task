#opening balance
print("Welcome to Kiran Bank")

balance = 10000

print("Opening Balance: Rs.", balance)


#deposit
while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")
    
    #withdrawal
    print("Welcome to Kiran Bank")

balance = 10000

print("Opening Balance: Rs.", balance)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: Rs.", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance = balance + amount
                print("Deposit successful!")
                print("Updated Balance: Rs.", balance)
            else:
                print("Invalid amount! Enter an amount greater than 0.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount! Enter an amount greater than 0.")

            elif amount <= balance:
                balance = balance - amount
                print("Withdrawal successful!")
                print("Updated Balance: Rs.", balance)

            else:
                print("Insufficient balance!")
                print("Current Balance: Rs.", balance)

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using Kiran Bank!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
        
        
        #validation
        print("Welcome to Kiran Bank")

balance = 10000.0

print("Opening Balance: Rs.", balance)

while True:
    print("\n----- Banking Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        print("Your Current Balance: Rs.", balance)

    elif choice == "2":
        amount_text = input("Enter deposit amount: ").strip()

        try:
            amount = float(amount_text)

            if amount <= 0:
                print("Invalid amount! Enter an amount greater than 0.")
            else:
                balance = balance + amount
                print("Deposit successful!")
                print("Updated Balance: Rs.", balance)

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "3":
        amount_text = input("Enter withdrawal amount: ").strip()

        try:
            amount = float(amount_text)

            if amount <= 0:
                print("Invalid amount! Enter an amount greater than 0.")

            elif amount > balance:
                print("Insufficient balance!")
                print("Available Balance: Rs.", balance)

            else:
                balance = balance - amount
                print("Withdrawal successful!")
                print("Remaining Balance: Rs.", balance)

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using Kiran Bank!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
        
        
        
        #menu loop
        # Q3: Banking Console Application - Menu Loop

balance = 10000

print("Welcome to Kiran Bank")
print("Opening Balance: ₹", balance)

while True:
    print("\n----- Main Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance = balance + amount
                print("Deposit successful!")
                print("Updated Balance: ₹", balance)
            else:
                print("Invalid amount! Enter an amount greater than 0.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Invalid amount! Enter an amount greater than 0.")
            elif amount <= balance:
                balance = balance - amount
                print("Withdrawal successful!")
                print("Updated Balance: ₹", balance)
            else:
                print("Insufficient balance!")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using Kiran Bank. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
