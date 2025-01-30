def simple_atm():
    balance = 1000  # Starting balance

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
       
        # Get user input for menu choice
        choice = int(input("Enter your choice (1/2/3/4): "))

        # Check the choice and perform actions
        if choice == 1:
            print(f"Your balance is: ${balance}")

        elif choice == 2:
            deposit = float(input("Enter deposit amount: $"))
            balance += deposit
            print(f"You deposited: ${deposit}. Your new balance is: ${balance}")

        elif choice == 3:
            withdraw = float(input("Enter withdrawal amount: $"))
            if withdraw <= balance:
                balance -= withdraw
                print(f"You withdrew: ${withdraw}. Your new balance is: ${balance}")
            else:
                print("Insufficient balance!")

        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid choice, please try again.")

# Run the simple ATM system
simple_atm()
