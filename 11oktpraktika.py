#-------------------------------1----------------------------------------
# class user:
#     def __init__(self,name,age,balance:int) -> None:
#          self.name = name
#          self.age = age
#          self.balance = balance
#     def getBalance(self):
#         return self.balance
#     def addMoney(self,money):
#         self.balance += money
#     def getMoney(self,money: int):
#         if self.balance > money:
#             print("Pul yechildi")
#             self.balance -= money
#         else:
#             print("Balanceda buncha pul yuq.")
#     def info(self) -> str:
#         print(f"Name:{self.name}\nAge:{self.age}\nBalance:{self.balance}")
    
# m1 = user(input("Ismingizni kiriting: "),int(input("Yoshingizni kiriting: ")),int(input("Balansni kiriting: ")))
# print("Menu\n1.add money\n2.get money\n3.Get balance\n4.Exit")
# a = int(input(">>>> "))
# if a == 1:
#     money = int(input("Pulni kiriting: "))
#     m1.addMoney(money)
# elif a == 2:
#     u_money = int(input(">>>> "))
#     m1.getMoney(u_money)
# elif a == 3:
#     print(m1.getBalance())
# print(m1.info())
#-----------------------------------2------------------------------------------
# class market:
#     def __init__(self,name,money,adress) -> None:
#         self.product = product = {
#             'olma' : 500,
#             'anor' : 600,
#             'banan' : 600
#         }
#         self.name = name 
#         self.money = money
#         self.address = adress
#         self.balance = 1000
#     def getProduct(self):
#         for i in self.product.items():
#             print(str(i))
#     def addProduct(self,name,money):
#         self.product.update({name:money})
#     def removeProduct(self,name):
#         if name in self.product:
#             self.product.pop(name)
#         else:
#             print("No remove product")
#     def sell(self,name,son):
#         a = self.product[name]
#         b = a * son
#         self.balance += b
#     def addMoney(self):
#         return self.balance
#     def info(self):
#         print(f"{self.balance}")

# user = market(input("Enter you name: "),int(input("Enter you age: ")),input("Address: "))
# while True:
#     print("Menu\n1.getProduct\n2.addProduct\n3.sell\n4.balance\n5.Remove product")
#     a = int(input(">>>> "))
#     if a == 1:
#         user.getProduct()
#     elif a == 2:
#         user.addProduct(input("Product name: "),int(input("Product money: ")))
#     elif a == 3:
#         user.sell(input("Product name: "),int(input("Product son: ")))
#     elif a == 4:
#         print(user.info())
#     elif a == 5:
#         user.removeProduct(input("Remove product name: "))
#-------------------------------------3----------------------------
class company:
    def __init__(self,name,location,establishedAT,balance) -> None:
        self.name = name
        self.locat = location
        self.estab = establishedAT
        self.balance = balance

    def getName(self):
        return self.name
    def getLocation(self):
        return self.locat
    def getBalance(self):
        return self.balance
    
class CarComany(company):
    def __init__(self, name, location, establishedAT, balance,cars) -> None:
        super().__init__(name, location, establishedAT, balance)
        self.cars = cars
    def getCarsCount(self):
        pass
    def addCar(self):
        pass
    def sellCar(self):
        pass
    def getallCars(self):
        pass

class MeatCompany(company):
    def __init__(self, name, location, establishedAT, balance,allMeatkg) -> None:
        super().__init__(name, location, establishedAT, balance)
        self.allMeat = allMeatkg
    def addMeat(self):
        pass
    def sellCar(self):
        pass

class SillCompany(company):
    def __init__(self, name, location, establishedAT, balance,simCards) -> None:
        super().__init__(name, location, establishedAT, balance)
        self.simCards = simCards
    def sellSimcard(self):  
        pass
    def addSimcards(self):
        pass
    def getSimcards(self):
        pass
