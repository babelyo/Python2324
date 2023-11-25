class Account:
    def __init__(self, name, balance, incoming_transfer_fee=0):
        self.name = name
        self.balance = balance
        self.incoming_transfer_fee = incoming_transfer_fee

    def tranfer(self, target_account, amount):
        self.balance -= amount
        target_account.balance += amount - target_account.incoming_transfer_fee
        print(f'{self.name} transfers {amount} PLN to {target_account.name}')

    def show_balance(self):
        print(f'{self.name} has actualy {self.balance} PLN')


asia_account = Account("Asia", 100, 1)
basia_account = Account("Basia", 100)
pawel_account = Account("Pawel", 100)

asia_account.tranfer(pawel_account,20)
basia_account.tranfer(pawel_account, 50)
pawel_account.tranfer(asia_account, 60)
basia_account.tranfer(asia_account, 30)

asia_account.show_balance()
basia_account.show_balance()
pawel_account.show_balance()
