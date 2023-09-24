from ATMmachine import ATM

ATM = ATM()

while True:
    print("ATM Menu:")
    print("1. Register User")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        pin_code = input("Enter your PIN code: ")
        ATM.register_user(name, pin_code)

    elif choice == "2":
        name = input("Enter your name: ")
        pin_code = input("Enter your PIN code: ")
        user = ATM.login_user(name, pin_code)
        if user:
            while True:
                print(f"Welcome, {user.username}!")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Logout")

                option = input("Enter your option: ")

                if option == "1":
                    print(f"Current Balance: {user.check_balance()} USD\n")

                elif option == "2":
                    try:
                        amount = float(input("Enter the amount to deposit: "))
                        if amount <= 0:
                            print("Invalid amount. Please enter a positive value.\n")
                        else:
                            if user.deposit_money(amount):
                                print(f"Deposited {amount} USD into your account.\n")
                            else:
                                print("Invalid amount. Please enter a positive value.\n")
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric value.\n")

                elif option == "3":
                    try:
                        amount = float(input("Enter the amount to withdraw: "))
                        if amount <= 0:
                            print("Invalid amount. Please enter a positive value.\n")
                        elif not user.withdraw_money(amount):
                            print("Insufficient funds or invalid amount.\n")
                        else:
                            print(f"Withdrew {amount} USD from your account.\n")
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric value.\n")

                elif option == "4":
                    print(f"Logging out {user.username}. Goodbye!\n")
                    break

                else:
                    print("Invalid option. Please enter a valid option.\n")

    elif choice == "3":
        ATM.save_data()
        print("Exiting the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.\n")