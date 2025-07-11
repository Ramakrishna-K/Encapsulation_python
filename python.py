
#  2. Encapsulation
#  Hiding the internal state and requiring all interaction through methods.

#  Use _ (protected) or __ (private) prefixes.



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner            # public
        self.__balance = balance      # "private" attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance is {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance   # ✅ corrected line

# Usage
acct = BankAccount("Alice", 100)
acct.deposit(60)
print(acct.get_balance())
