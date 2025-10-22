# ATM machine logic : Ask the user for amount to withdraw.
# If amount ≤ balance → allow withdrawal.
# If amount > balance → print "Insufficient Funds".

valid_AccountNumber="234"
valid_Password="9876"
accountNumber=input("Enter Account Number :- ")

if accountNumber == valid_AccountNumber:
    enteredPassword=input("Enter Password :- ")
    if enteredPassword==valid_Password:
        currentBalance=10500

        print("Access Granted for Account Number :- ",accountNumber)
        print(currentBalance)
        transactionType=input("Enter Transaction Type (withdraw or deposit) ")
        amount=int(input("Enter amount :  ₹ "))

        if transactionType=="withdraw":
            if amount <= currentBalance:
                currentBalance=currentBalance-amount
                print("Withdrawn Successfully")
                print("current balance ",currentBalance)
            else:
                print("Insufficient funds. Transaction declined.")
        elif transactionType == "deposit":
            currentBalance+=amount
            print("Deposit Successfully")
            print("New Current Balance ",currentBalance)
        else:
            print("Invalid transaction type. Please enter 'withdraw' or 'deposit'.")
    else:
        print("\n Password invalid. Access denied.")
else:
    print("\n Invalid account number. Access denied.")