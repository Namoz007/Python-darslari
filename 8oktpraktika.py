#-----------------------------1----------------------------
# from typing import Any

# class Human:
#     def __init__(self,firstname: str,lastname: str,id:int,salary: int) -> None:
#         self.frname = firstname
#         self.lsname = lastname
#         self.id = id
#         self.sl = salary
#     def getId(self):
#         return self.id
#     def getFirstname(self):
#         return self.frname
#     def getLastname(self):
#         return self.lsname
#     def getSalary(self):
#         return self.sl
#     def getName(self):
#         return f"{self.frname} {self.lsname}"
#     def setSalary(self,salary: int):
#         self.sl = salary
#         return self.sl
#     def getAnualsalary(self):
#         return self.sl * 12
#     def raiseSalary(self,precent: int):
#         a = self.sl
#         b = a % 100
#         c = a * precent
#         self.sl += c
#         # return self.sl
#     def __str__(self) -> str:
#         return f"Name:{self.frname}\nSurname:{self.lsname}\nID:{self.id}\nSalary:{self.sl}"

# odam = Human("Muhammadzohid",'Qahramonov',16771,500)
# odam.raiseSalary(15)
# print(odam)
#---------------------------2---------------------------------
# from typing import Any


# class Circle:
#     def __init__(self,radius: int,color: str) -> None:
#         self.rad = radius
#         self.cl = color
#         self.p = 3.14
#     def getRadius(self):
#         return self.rad
#     def setRAdius(self,radius: int):
#         self.rad = radius
#     def getColor(self):
#         return self.cl
#     def setColor(self,color: str):
#         self.cl = color
#     def getArea(self):
#         return (self.rad ** 2) * self.p
#     def circumference(self):
#         return 2 * self.p * self.rad
#     def getInfo(self):
#         return f"Radius: {self.rad}\nColor:{self.cl}\nArea:{(self.rad ** 2) * self.p}\nArea length:{2 * self.p * self.rad}"
# user = Circle(5,"green")
#------------------------------3------------------------------
# class Restangle:
#     def __init__(self,height,width,) -> None:
#         self.h = height
#         self.w = width
#     def getHeight(self):
#         return self.h
#     def setHeight(self,height):
#         self.h = height
#     def getWidth(self):
#         return self.w
#     def setWidth(self,width):
#         self.w = width
#     def getArea(self):
#         return self.h * self.w
#     def getPerim(self):
#         return ((self.h * 2) + (self.w * 2))
#     def getInfo(self):
#         return f"Height:{self.h}\nWidth:{self.w}\nArea:{self.h * self.w}\nPerimetr:{((self.h * 2) + (self.w * 2))}"
    
# user = Restangle(10,5)
#-----------------------------------4-------------------------------
# class Accaunt:
#     def __init__(self,id: str,name: str,balance:int) -> None:
#         self.id = id
#         self.n = name
#         self.b = balance
#     def getId(self):
#         return self.id
#     def getName(self):
#         return self.n
#     def getBalancer(self):
#         return self.b
#     def credit(self,balance: int):
#         self.b += balance
#     def debit(self,amount):
#         if self.b > amount:
#             self.b -= amount
#         else:
#             print("Akkauntingda buncha mablag' mavjud emas.")
#     def transferTo(self,account,amount):
#         if self.b > amount:
#             print(f"{account}ga mana shuncha mablag' otkazildi.")
#         else:
#             print("Akkauntingda buncha mablag' yuq.")
#     def __str__(self) -> str:
#         return f"Id:{self.id}\nName:{self.n}\nBalance:{self.b}"
# user = Accaunt("167771","Muhammadzohid",1500000)
# user.credit(150000)
# print(user)
#-------------------------------5--------------------------

# class Date:
#     def __init__(self,day:int,month:int,year:int) -> None:
#         self.d = day
#         self.m = month
#         self.y = year
#     def getDay(self):
#         return self.d
#     def getMonth(self):
#         return self.m
#     def getYear(self):
#         return self.y
#     def setDay(self,day):
#         self.d = day
#     def setMonth(self,month):
#         self.m = month
#     def setYear(self,year):
#         self.y = year
#     def setDate(self,day,month,year):
#         self.d = day
#         self.m = month
#         self.y = year
#     def getInfo(self):
#         return f"{self.d}:{self.m}:{self.y}"
        