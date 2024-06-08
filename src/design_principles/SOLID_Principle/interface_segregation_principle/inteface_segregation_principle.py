"""
Typical violation
A typical violation of the Interface Segregation Principle
    is given in Agile Software Development:
Principles,
Patterns,
Practices in 'ATM Transaction example' and
   in an article also written by Robert C. Martin specifically about the ISP.
This example discusses the User Interface for an ATM,
   which handles all requests such as a deposit request,
  or a withdrawal request,
   and how this interface needs to be segregated into
  individual and more specific interfaces.
"""


class BankAccount:

    def __init__(self, color, board):
        pass

    def deposit(self):
        pass

    def balance(self):
        pass

    def withdraw(self):
        pass


class BankAccountProxy:
    def __init__(self, account: BankAccount):
        self.account = account

    def deposit(self):
        pass

    def balance(self):
        pass

    def withdraw(self):
        pass


class OnlyWithdrawOperator:
    def __init__(self, proxy: BankAccountProxy):
        self.account = account

    def withdraw(self):
        pass

    def balance(self):
        pass


class OnlyDepositOperator:
    def __init__(self, proxy: BankAccountProxy):
        self.account = account

    def deposit(self):
        pass


# Then
class POS(OnlyDepositOperator):
    pass
