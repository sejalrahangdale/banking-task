print("Welcome to Kiran Bank")

balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Invalid amount!")

            else:
                balance = balance + amount
                print("Deposit successful!")
                print("Updated Balance:", balance)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount!")

            elif amount > balance:
                print("Insufficient balance!")

            else:
                balance = balance - amount
                print("Withdrawal successful!")
                print("Remaining Balance:", balance)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        print("Thank you for using Kiran Bank!")
        break
    
    
    #invalid menu
    else:
        print("Invalid choice! Please select 1 to 4.")
        


    
        
        
        
    
        