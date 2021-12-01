class User:
    def __init__(self, name, balance, email="") -> None:
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, ammount):
        self.balance += ammount
        return self


    def make_withdraw(self, ammount):
        self.balance -= ammount
        return self

    def display_user_balance(self):
        print(self.balance)
    
    def transfer_money(self, friend, ammount):
        self.balance -= ammount
        friend.balance += ammount
        print(f"My balance: {self.balance} Friend's Balance: {friend.balance}")



user1 = User("Craig", 777)
user2 = User("KevBot", 1000)
user3 = User("Austin", 1200)

user1.make_deposit(500).make_deposit(600).make_deposit(700).make_withdraw(1477).display_user_balance()
user2.make_deposit(4000).make_deposit(4000).make_withdraw(1477).make_withdraw(1477).display_user_balance()
user3.make_deposit(4000).make_withdraw(1477).make_withdraw(1477).make_withdraw(1477).display_user_balance()

user1.transfer_money(user2, 500)