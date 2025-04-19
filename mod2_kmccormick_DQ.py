# Simulated banking account data
account = {
    "balance": 5000,
    "daily_limit_remaining": 1000,
    "monthly_limit_remaining": 10000,
    "yearly_limit_remaining": 50000,
    "is_restricted": False
}

# --- Condition Functions ---
def has_sufficient_funds(account, amount):
    print("Checking for sufficient funds...")
    return account["balance"] >= amount

def within_transaction_limits(account, amount):
    print("Checking transaction limits...")
    return (account["daily_limit_remaining"] >= amount and
            account["monthly_limit_remaining"] >= amount and
            account["yearly_limit_remaining"] >= amount)

def is_not_restricted(account):
    print("Checking account restrictions...")
    return not account["is_restricted"]

def process_transaction(account, amount):
    print(f"✅ Transaction of ${amount:.2f} approved!")
    # Simulate debiting the account
    account["balance"] -= amount
    account["daily_limit_remaining"] -= amount
    account["monthly_limit_remaining"] -= amount
    account["yearly_limit_remaining"] -= amount


# --- Main Program Logic ---
print("💳 Welcome to Your Bank!")

try:
    user_input = input("Enter transaction amount: $")
    transaction_amount = float(user_input)

    print("\n--- Transaction Attempt ---")
    if transaction_amount <= 0:
        print("Invalid amount. Must be greater than 0.")
    elif has_sufficient_funds(account, transaction_amount) and \
         within_transaction_limits(account, transaction_amount) and \
         is_not_restricted(account):
        process_transaction(account, transaction_amount)
    else:
        print("Transaction denied due to one or more conditions failing.")

except ValueError:
    print("Invalid input. Please enter a numeric amount.")