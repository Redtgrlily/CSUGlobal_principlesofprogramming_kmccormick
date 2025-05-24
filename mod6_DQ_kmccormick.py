user_account = {
    "account_id": "A1020",
    "name": "John Smith",
    "balance": 14000.28,
    "currency": "USD"
}

user_account["status"] = "active"
print("User Account:", user_account)

user_account["balance"] -= 200.00
user_account.update({"currency":"USD"})
print("Updated Account:", user_account)

del user_account["status"]
currency = user_account.pop("currency")
print("Final Account Info:", user_account)
print("Currency Removed:", currency)