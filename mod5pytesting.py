account_balance = 1200
credit_score = 710
has_collateral = False

# Using AND: customer must meet both criteria
if account_balance > 1000 and credit_score > 700:
    print("Loan approved based on balance and credit score.")
else:
    print("Loan not approved based on balance and credit score.")

# Using OR: customer can qualify by either having enough balance or having collateral
if account_balance > 1000 or has_collateral:
    print("Loan approved based on balance or collateral.")
else:
    print("Loan not approved.")