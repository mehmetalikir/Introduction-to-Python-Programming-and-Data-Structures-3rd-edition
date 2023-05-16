class Account():
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def setId(self, id):
        self.id = id

    def setBalance(self, balance):
        self.balance = balance

    def getId(self, id):
        return self.id

    def getBalance(self, id):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
