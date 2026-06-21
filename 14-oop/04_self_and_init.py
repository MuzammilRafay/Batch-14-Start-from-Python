class FeeAccount:
    def __init__(self, balance):
        self._balance = balance # _ variable ya attribute private for this class

    def pay(self, amount):
        if amount <= 0:
            return "Invalid payment"
        self._balance = max(0, self._balance - amount)
        return "Payment accepted"

    def get_balance(self):
        return self._balance
    
account = FeeAccount(5000)
print(account.pay(2000))
print("Balance:", account.get_balance())
