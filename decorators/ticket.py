def check_balance(func):
    balance = 200
    def wrapper(amt):
        print("Transaction has started...")
        if amt <= balance:
            func(amt)
            print("Please collect your Ticket.")
        else:
            print("Sufficient balance is required to complete the Transaction!")
        print("Transaction completed.")
        print("Have a good day")
    return wrapper
            


@check_balance
def purchase_ticket(amount):
    print(f"processing ticket with {amount}/- rupees")
    
purchase_ticket(200)