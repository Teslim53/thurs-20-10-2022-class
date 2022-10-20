# assumed user balance
user_balance = 1234.55

# assumed user password
user_password = "!2A34"


print("Welcome to Trusted Bank ATM")
print("1. Withdraw")
print("2. Exit")
print("3. Deposit")

choice = int(input("Enter 1, 2 or 3: "))
if choice == 1:
    inputted_password = input("Enter your password: ")
    if user_password==inputted_password:
        amount = float(input("Enter the amount you want to withdraw: "))
        print("amount")
        # TODO 1: Check if the amount is greater than the user balance
        # If so, print "Take your money" and deduct the amount from the user's balance
        # Also print the new balance.
        # Otherwise, print "Insufficient funds"
        if amount<=user_balance and amount>0:
            print("Take your money")
            user_balance = (user_balance-amount)
            print(f"Your new balance is ${user_balance:.2f}")
        else:
            print("Insufficient funds")
    else:
        print("Incorrect password!")

# TODO 2: Check if the choice is 2
# If so, print "Thank you for using our ATM"
# Otherwise, print "Invalid choice"
elif choice==2:
    print("Thank you for using our ATM")
elif choice==3:
    amount_to_deposit = float(input("Enter the amount you wish to deposit: "))
    if amount_to_deposit>0:
        user_balance+=amount_to_deposit
        print(f"Your new balance is {user_balance:.2f}")
    else:
        print("You cannot deposit a negative amount!")

else:
    print("Invalid choice")


# TODO 3 (Bonus): Check if the user password is correct before implementing the withdraw logic
# TODO 4 (Bonus): Add a deposit option to the ATM
# a deposit should ask for the amount, add money to the user's balance and print the new balance
