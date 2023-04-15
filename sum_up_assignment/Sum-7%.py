import sys

def sumall():
    money_list = []
    for i in range(10):
        money = int(input(f"Enter Amount {i+1}: "))
        money_list.append(money)
    print("The numbers you entered are:", money_list)

    my_set = set(money_list)  # Convert list to set to remove duplicates
    print(f"{my_set} sorted figures")

    total_amount = sum(my_set)  # Compute the sum of the remaining numbers
    print(f"{total_amount} the sum result")

    VAT = 0.07  # assuming VAT is 7% expressed as a decimal
    request_Withdrawal = input("Would you like to make a withdrawal from your wallet balance? Type yes else type no ")

    if request_Withdrawal.lower() != 'yes':
        print("thank you for investing with us.")
        sys.exit()

    withdrew = int(input("Input amount to withdraw: N"))
    amount_with_vat = withdrew + (withdrew * VAT)

    if withdrew > total_amount:
        print("Amount Exceeds Your Balance.")
        sys.exit()

    if amount_with_vat > total_amount:
        print("You cannot withdraw up to that amount (7% VAT inclusive).")
        sys.exit()
    else:
        total_amount -= amount_with_vat
        print(f"Successful withdrawal. 7% VAT has been deducted from your wallet balance, current balance now: N{total_amount}")

        print("Hello! We are always here to serve you and to give you the best service. Please don't forget to reach out to us whenever you have an issue!")
        sys.exit()

sumall()
