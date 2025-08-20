# prompt the user to insert a coin

def amount_due():
    coke_price = 50  # Price of the coke in cents
    total_paid = 0

    while total_paid < coke_price:
        try:
            paid_amount = int(input("How much are you paying for the coke? "))
            total_paid += paid_amount
            
            amount_left = coke_price - total_paid
            if amount_left > 0:
                print(f"Amount still due: {amount_left} cents")
            else:
                change = abs(amount_left)
                print(f"Change owed: {change} cents")

        except ValueError:
            print("Invalid input. Please enter a valid amount.")


amount_due()
