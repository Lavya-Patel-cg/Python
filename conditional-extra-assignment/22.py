account_balance=int(input("Enter account balance:-"))
withdrawal_amount=int(input("Enter withdrawal amount:-"))
if withdrawal_amount<0 or withdrawal_amount%100!=0:
    print("Invalid")
elif withdrawal_amount>account_balance:
    print("Invalid input")

elif (account_balance-withdrawal_amount)<=500:
    print("500Rs must remain in the account")

elif account_balance-withdrawal_amount>500:
    print("Withdrawal successful")

    Remaining_balance=account_balance-withdrawal_amount
    print("Remaining balance:-",Remaining_balance)  