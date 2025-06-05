import uuid
class DemographicProfile:
    def __init__(self, name, age, income, region):
        self.__member_id = str(uuid.uuid4())
        self.__name = name
        self.__age = age
        self.__income = income
        self.__region = region
        
    def get_member_id(self):
        return self.__member_id
    
    def get_summary(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "income": self.__income,
            "region": self.__region
        }

class Member:
    def __init__(self, profile: DemographicProfile):
        self.member_id = profile.get_member_id()
        
    def display_reference(self):
        print(f"Member ID: {self.member_id}")

class BankAccount:
    def __init__(self, member_id, initial_balance=0):
        self.member_id = member_id
        self.__balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance  -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            
    def get_balance(self):
        return self.__balance
    
    def account_summary(self):
        return {
            "member_id": self.member_id,
            "balance": self.__balance
        }

user_profile = DemographicProfile("Alice", 34, 95000, "East Coast")

member = Member(user_profile)

account = BankAccount(member.member_id, initial_balance=1000)

member.display_reference()
account.deposit(500)
account.withdraw(300)

print(account.account_summary())
    