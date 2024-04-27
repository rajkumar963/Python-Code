#Bank Account ,tittle, deposit, withdraw, balance, account number
# class BankAccount:
#     def __init__(self, title, balance, account_number):
#         self.__title = title
#         self.__balance = balance
#         self.__account_number = account_number

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return True
#         return False

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             return True
#         return False

#     def get_account_info(self):
#         return f"Account Title: {self.__title}, Account Number: {self.__account_number}, Balance: {self.__balance}"


# # Example usage
# account = BankAccount("John Doe", 1000, "123456")
# print(account.get_account_info())  

# account.deposit(500)
# print(account.get_balance())  

# account.withdraw(200)
# print(account.get_balance())  

########################################################################################

# class BankAccount:
#     def __init__(self, account_number, title, balance=0):
#         self.__account_number = account_number
#         self.__title = title
#         self.__balance = balance

#     def __deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited {amount} into account {self.__account_number}. New balance: {self.__balance}")

#     def __withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             print(f"Withdrew {amount} from account {self.__account_number}. Remaining balance: {self.__balance}")
#         else:
#             print(f"Insufficient funds in account {self.__account_number}. Current balance: {self.__balance}")

#     def __get_balance(self):
#         print(f"Account {self.__account_number} ({self.__title}) balance: {self.__balance}")

# # Example usage
# account1 = BankAccount("123456789", "Savings Account", 1000)
# account2 = BankAccount("987654321", "Checking Account")

# account1._BankAccount__deposit(500)
# account2._BankAccount__withdraw(200)
# account1._BankAccount__get_balance()
# account2._BankAccount__get_balance()
# account2._BankAccount__withdraw(1000)


#################################################################

#add ,sub ,mul ,div in complex number

# class Complex:
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
#     def __add__(self,other):
#         real=self.real+other.real
#         imag=self.imag+other.imag
#         return Complex(real,imag)
#     def __sub__(self,other):
#         real=self.real-other.real
#         imag=self.imag-other.imag
#         return Complex(real,imag)
#     def __mul__(self,other):
#         real=(self.real*other.real - self.imag * other.imag)
#         imag=self.real*other.imag+self.imag*other.real
#         return Complex(real,imag)
#     def __truediv__(self,other):
#         real=(self.real*other.real+self.imag*other.imag)/(other.real**2+other.imag**2)
#         imag=(self.imag*other.real-self.real*other.imag)/(other.real**2+other.imag**2)
#         return Complex(real,imag)
    

# a = Complex(2, 3)
# b = Complex(1,2)    
# c = a + b
# print(c.real, c.imag)
# d = a - b
# print(d.real, d.imag)
# e = a * b
# print(e.real, e.imag)
# f = a / b
# print(f.real, f.imag)

##############################################################################

#car class model, color, company, price,engine
class Car:
    def __init__(self, model, color, company, price, engine):
        self.__model = model
        self.__color = color
        self.__company = company
        self.__price = price
        self.__engine = engine

    def getCar(self):
        return self.__model 
    
    def setCar(self, model):
        self.__model = model

    def getCarColor(self):
        return self.__color
    
    def setCarColor(self, color):
        self.__color = color

    def getCarCompany(self):
        return self.__company
    
    def setCarCompany(self, company):
        self.__company = company

    def getCarPrice(self):
        return self.__price
    
    def setCarPrice(self, price):
        self.__price = price

    def getCarEngine(self):
        return self.__engine
    
    def setCarEngine(self, engine):
        self.__engine = engine


