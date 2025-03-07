from decimal import Decimal

class Wallet:
    @classmethod
    def transfer_funds(self, source_account: "Account", destination_account: "Account", amount: Decimal):        
        source_account.withdraw(amount)
        destination_account.deposit(amount)
    

class User:
    def __init__(self, first_name):
        self.first_name = first_name


class Account:
    def __init__(self, user):
        self.user = user
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("not enough funds")


print("Enter wallet users")

user_name_1 = input("Enter 1st user  name: ")
user_1 = User(first_name=user_name_1)

user_name_2 = input("Enter 2nd user name: ")
user_2 = User(first_name=user_name_2)

account_1 = Account(user=user_1)
account_2 = Account(user=user_2)


print("1st user balance:", account_1.balance)
print("2st user balance:", account_2.balance)

# ask to deposit 
print()
print("Please deposit money")
amount = int(input("Enter amount to deposit: "))
account_1.deposit(amount)


print()
amount = int(input("How much to send to account_2: "))

print("Transferring fund from account_1 to account_2...")
Wallet.transfer_funds(
    source_account=account_1,
    destination_account=account_2,
    amount=amount
)
print()


print("Balance after operation:")
print("1st user balance:", account_1.balance)
print("2st user balance:", account_2.balance)

