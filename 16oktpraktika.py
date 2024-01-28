#-----------------------------1-masala--------------------------------
from abc import ABC,abstractmethod
# class shakl(ABC):
#     @abstractmethod
#     def yuza(self):
#         pass
    
# class togritortburchak(shakl):
#     def __init__(self,yon,tepa) -> None:
#         self.yon = yon
#         self.tepa = tepa
    
#     def yuza(self):
#         print(f"To'g'rito'rtburchak yuzasi: {self.yon * self.tepa}")

#     def perimetr(self):
#         print(f"Bu to'g'ri to'rtburchak perimetri: {(self.tepa * 2) + (self.yon * 2)}")

# class tortburchak(shakl):
#     def __init__(self,chap,ong,tepa,past) -> None:
#         self.past = past
#         self.tepa = tepa
#         self.ong = ong
#         self.chap = chap
    
#     def yuza(self):
#         print(f"Bu tortburchak yuzasi: {(self.ong + self.tepa) * 2} sm2")
    
#     def perimetr(self):
#         print(f"Bu tog'ri to'rtburchak perimetri : {self.ong + self.chap + self.tepa + self.past} sm")

#     def burchaklar(self):
#         bir = int(input("Birinchi burchak gradusini kiriting: "))
#         ikki = int(input("Ikkinchi burchak gradusini kiriting: "))
#         uch = int(input("Uchinchi burchak gradusini kiriting: "))

#         print(f"Tortinchi burchak : {360 - (bir + ikki + uch)} gradus.")

# class dumaloq(shakl):
#     def __init__(self,radius) -> None:
#         self.radius = radius
#         self.p = 3.14
#         self.diametr = self.radius * self.p

#     def yuza(self):
#         print(f"Bu dumaloq yuzasi: {self.radius * self.diametr}")
    
#     def vatar(self):
#         print(f"Bu dumaloq vatari: {self.diametr}")

# class uchburchak(shakl):
#     def __init__(self,bir_tomon,ikki_tomon,uch_tomon,balandligi) -> None:
#         self.bir_tom = bir_tomon
#         self.ikki_tom = ikki_tomon
#         self.uch_tom = uch_tomon
#         self.baland = balandligi

#     def yuza(self):
#         print(f"Bu uchburchak yuzasi: {0.5 * self.baland * max(self.bir_tom,self.ikki_tom,self.uch_tom)}")
    
#     def burchak(self):
#         bir = int(input("Birinchi burchak gradusi: "))
#         ikki = int(input("IKkinchi burchak gradusi: ")) 
#         print(f"Bu uchburchakning uchinchi gradusi : {180 - (bir + ikki)}")
#------------------------------2-masala------------------------------------
class Human(ABC):
    @abstractmethod
    def getAge(self):
        pass

    @abstractmethod
    def getHeight(self):
        pass

    @abstractmethod
    def getKg(self):
        pass

    @abstractmethod
    def getBirthday(self):
        pass

class school(Human):
    def __init__(self,firstname,secondname,address,birtday,height,weight,read_address,age) -> None:
        self.firstname = firstname
        self.secondname = secondname
        self.address = address
        self.birthday = birtday
        self.height = height
        self.weight = weight
        self.read = read_address
        self.age = age
    
    def getAge(self):
        print(f"Age : {self.age}")

    def getHeight(self):
        print(f"Height : {self.height}")

    def getKg(self):
        print(f"Wegiht : {self.weight}")

    def getBirthday(self):
        print(f"Birthday : {self.birthday}")

    def getAcademy(self):
        print(f"Academy : {self.read}")
    
    def getEat(self):
        print(f"I can eat.")
    
    def getRun(self):
        print("I can get run.")
    
    def write(self):
        print("I can wite")
    
    def read(self):
        print("I can read a book.")

class kindergardom(Human):
    def __init__(self,firstname,secondname,address,birtday,height,weight,read_address,age) -> None:
        self.firstname = firstname
        self.secondname = secondname
        self.address = address
        self.birthday = birtday
        self.height = height
        self.weight = weight
        self.read = read_address
        self.age = age
    
    def getAge(self):
        print(f"Age : {self.age}")

    def getHeight(self):
        print(f"Height : {self.height}")

    def getKg(self):
        print(f"Wegiht : {self.weight}")

    def getBirthday(self):
        print(f"Birthday : {self.birthday}")

    def getAcademy(self):
        print(f"Academy : {self.read}")
    
    def getEat(self):
        print(f"I can eat.")
    
    def getRun(self):
        print("I can get run.")

    def game(self):
        print("I can play toys.")
    
    def paint(self):
        print("I can paint.")

    def yiglamoq(self):
        print("cry.")
    
    def speek(self):
        print("I can speek.")
    
class child(Human):
    def __init__(self,firstname,secondname,address,birtday,height,weight,age) -> None:
        self.firstname = firstname
        self.secondname = secondname
        self.address = address
        self.birthday = birtday
        self.height = height
        self.weight = weight
        self.age = age

    def getAge(self):
        print(f"Age : {self.age}")

    def getHeight(self):
        print(f"Height : {self.height}")

    def getKg(self):
        print(f"Wegiht : {self.weight}")

    def getBirthday(self):
        print(f"Birthday : {self.birthday}")
    
    def getEat(self):
        print(f"I can eat.")
    
    def cry(self):
        print("Cry")
# class teenager(Human):