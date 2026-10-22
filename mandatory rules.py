

balance = 0.0
choice = ""

print("===== Welcome to Simple Bank =====")

while choice != "4":
    print()
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        print("Current balance: Rs.", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Deposit failed. Please enter a valid number.")
        else:
            if amount <= 0:
                print("Deposit failed. Amount must be greater than zero.")
            else:
                balance = balance + amount
                print("Rs.", amount, "deposited. New balance: Rs.", balance)

    elif choice == "3":
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Withdrawal failed. Please enter a valid number.")
        else:
            if amount <= 0:
                print("Withdrawal failed. Amount must be greater than zero.")
            elif amount > balance:
                print("Withdrawal failed. Insufficient balance. Available: Rs.", balance)
            else:
                balance = balance - amount
                print("Rs.", amount, "withdrawn. New balance: Rs.", balance)

    elif choice == "4":
        print("Thank you for banking with us. Final balance: Rs.", balance)

    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")