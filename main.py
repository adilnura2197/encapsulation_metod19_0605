class Bank:
    def __init__(self, balance):
        self._balance = balance


class Card(Bank):
    def __init__(self, balance, pin):
        super().__init__(balance)
        self.__pin = pin

    def deposit(self, x):
        self._balance += x

    def withdraw(self, pin, x):
        if self.__pin == pin:
            self._balance -= x
        else:
            print("Wrong pin")

    def check_balance(self):
        print(self._balance)


c1 = Card(100, "1234")

c1.deposit(100)
c1.check_balance()

c1.withdraw("0000", 50)
c1.withdraw("1234", 50)
c1.check_balance()
