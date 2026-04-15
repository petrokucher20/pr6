class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner        # приватний атрибут
        self.__balance = balance    # приватний атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.__owner} deposited {amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        elif amount > 0:
            self.__balance -= amount
            print(f"{self.__owner} withdrew {amount}")
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance
acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 50)
acc3 = BankAccount("Charlie", 200)

# Тест acc1
acc1.deposit(50)
acc1.withdraw(30)
print("Balance:", acc1.get_balance())

# Тест acc2
acc2.withdraw(100)
acc2.deposit(20)
print("Balance:", acc2.get_balance())

# Тест acc3
acc3.deposit(100)
acc3.withdraw(50)
print("Balance:", acc3.get_balance())

