balance = 10000

print("Welcome to Kiran Bank")
print("Current Balance: ₹", balance)

#main menu
while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        print("Deposit Money")

    elif choice == "3":
        print("Withdraw Money")

    elif choice == "4":
        print("Thank you for using Kiran Bank!")
        break

    else:
        print("Invalid choice! Please try again.")
        
        
        #deposit money
        balance = 10000

print("Welcome to Kiran Bank")
print("Opening Balance: ₹", balance)

amount = int(input("Enter deposit amount: "))

if amount > 0:
    balance = balance + amount
    print("Deposit Successful!")
    print("Updated Balance: ₹", balance)
else:
    print("Invalid amount! Please enter an amount greater than 0.")


















    
    
    
    