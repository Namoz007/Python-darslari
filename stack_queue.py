#------------1-masala
# domino = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2], [2,3], [2,4], [2,5], [2,6], [3,3], [3,4], [3,5], [3,6], [4,4], [4,5], [4,6], [5,5], [5,6], [6,6]]
# input_dom = [[1,6], [6,3], [0,5], [5,2], [4,1], [3,5],[5,1], [4,5], [5,5], [2,6], [6,0], [0,1], [0,0], [2,2], [1,1], [1,3], [4,6], [4,4]]
# count = []
# for i in domino:
#     if i in input_dom:
#         pass
#     else:
#         count.append(i)
# print(count)


#-------------2-masala  
# a = input("Son kiriting: ")
# lst = []
# for i in a:
#     if i == '0':
#         lst.append(i)
#         lst.append(i)
#     else:
#         lst.append(i)
# print(lst)
#--------------4-masala  
with open("code.txt") as f:
    lst = []
    lst2 = []
    f.seek(0)
    for i in f.read().split():
        i += '_-'
        lst.append(i.split('-')[0])
    for i in lst:
        if len(i) > 3:
            if '+' in i and '=' in i and '1' in i:
                lst2.append('   ' + i[3] + '++' + i[-2] + '_')
            else:
                lst2.append(i)
        else:
            lst2.append(i)

with open('code.txt','w') as c:
    for i in lst2:
        a = i.split('_')[0]
        c.write(a + '\n')
# -------------------------------------------------------------------------------------------------------- #

#5---------------masala----
#Samandar aka shoshilyotganim shuning uchun database yaratish table yaratish, unga malumot qoshishlarni skreenshot qimadim, javobini wordda yozip tashavordim
#--------6-masala---
# class book:
#     def __init__(self,name: str,count_page: int,price: int) -> None:
#         self.name = name
#         self.count_page = count_page
#         self.price = price

#     def pricee(self):
#         if 'programming' in self.name.lower():
#             self.price += self.price
#         print(f"{self.name} kitobining narxi -- ${self.price}")
    
#     def averagePrice(self):
#         print(f"{self.name} kitobining bir sahifasi -- ${self.price / self.count_page}.")
    
# user_count = int(input("Nechta qiymat kiritmoqchisiz: "))
# users = []
# for i in range(user_count):
#     users.append(book(input("Enter your book name: "),int(input("Enter you book page: ")),int(input("Enter you book price: $"))))

# while True:
#     print("1.Bitta kitob sahifasini o'rtacha narxini bilish.   2.Kitoblarni narxini bilish.   3.Exit")
#     a = int(input(">>>> "))
#     if a == 1:
#         for i in users:
#             i.averagePrice()
        
#     elif a == 2:
#         for i in users:
#             i.pricee()
#     elif a == 3:
#         print("Thank you!")
#         break
#     else:
#         print("Not found!")
#-----------------7-masala----
# class Date:
#     def __init__(self,day: int,month:int,year: int):
#         self.day = day
#         self.month = month
#         self.year = year

# class Drug(Date):
#     def __init__(self, day: int, month: int, year: int,drug_name: str,date_create: str,company_name: str):
#         super().__init__(day, month, year)
#         self.drug_name = drug_name
#         self.date_create = date_create
#         self.company = company_name
    
#     def drug_about(self):
#         print(f"""
#             Drug name: {self.drug_name}
#             Drug date create: {self.date_create}
#             Drug create company: {self.company}  
#               """)
        
#     def days(self):
#         count = self.year - self.date_create
#         print(f"{self.drug_name} is {self.day} day,{self.month} month and {count} years create old!")

# user_count = int(input("How much count users: "))
# users = list()
# for i in range(user_count):
#     users.append(Drug(int(input("Now day: ")),int(input("Now month: ")),int(input("Now year: ")),input("Drug name: "),int(input("Drug create year: ")),input("Drug create company: ")))

# while True:
#     print("""
# 1.Drug about    2.Drug create old!  3.Exit
# """)
#     a = int(input(">>>> "))
#     if a == 1:
#         for i in users:
#             i.drug_about()
#     elif a == 2:
#         for i in users:
#             i.days()
#     elif a == 3:
#         print("Thank you!")
#         break
#     else:
#         print("Not found!")    
#--------------8-masala-------

#---------9-masala
# class ovozlar:
#     def __init__(self) -> None:
#         self.ovoz = []
#         self.ochirilganlar = []
#         self.ovoz_ism = []
#     def add(self,about,name):
#         self.ovoz.append(about)
#         self.ovoz_ism.append(name)
    
#     def nomzodlar(self):
#         for i in self.ovoz:
#             if len(self.ovoz) == 0:
#                 print("Xech qanaqa nomzodlar yuq!")
#             else:
#                 name = i.split("-")[0]
#                 ovoz = i.split("-")[1]
#                 print(f"{name} {ovoz} ta ovoz!")
    
#     def nomzodlarni_ochirish(self,ism):
#         ochirilgan = ''
#         count = self.ovoz_ism.count(ism)
#         if count == 0:
#             for i in self.ovoz:
#                 name = i.split("-")[0]
#                 if ism == name:
#                     self.ochirilganlar.append(i)
#                     self.ovoz.remove(i)
#                     print(f"{ism} nomzodlikdan chiqarip yuborildi.")
#                     break
#             print("Bunaqa nomzod mavjud emas!")
#         else:
#             print(f"Bunaqa foydalanuvchilar {count} ta.Siz o'chirmoqchi bo'lgan nomzodda nechta ovoz bor!")
#             a = int(input("Ovozni kiriting: "))
#             x = 0
#             for i in self.ovoz:
#                 new = i
#                 name = i.split("-")[0]
#                 ovozz = i.split("-")[1]
#                 if name == ism and a == int(ovozz):
#                     x += 1
#                     self.ochirilganlar.append(i)
#                     self.ovoz.remove(new)
#                     break
#             if x == 0:
#                 print('Bunaqa ovozli nomzod yoq!')

#     def kop_ovoz(self):
#         kop_ovozlar = []
#         if len(self.ovoz) > 0:
#             count = self.ovoz[0]
#             kop_ovozlar.append(count)
#             self.ovoz.remove(count)
#             for i in self.ovoz:
#                 ovoz1 = i.split("-")[1]
#                 ovoz2 = count.split("-")[1]
#                 if  int(ovoz1) == int(ovoz2):
#                     kop_ovozlar.append(i)
#                 elif int(ovoz1) == int(ovoz2):
#                     kop_ovozlar.remove(count)
#                     count = i
#             if len(kop_ovozlar) > 1:
#                 count = len(kop_ovozlar)
#                 print(f'{count} ta nomzodda bir xil ovoz bor!\nBular',end="")
#                 for i in kop_ovozlar:
#                     print(",",end="")
#                     print(f"{i.split('-')[0]} {i.split('-')[1]} ta ovoz",end="")
#                 print("!")
#             else:
#                 name = kop_ovozlar[0]
#                 print(f"Eng kop ovoz toplagan nomzod: {name.split('-')[0]} {name.split('-')[1]} ta ovoz!")       
#         else:
#             print("Hozircha nomzodlar mavjud emas!")


# user = ovozlar()
# while True:
#     print("""
# 1.Nomzod qo'shish.  2.Nomzodlar ro'yxati!   3.Nomzodni o'chirish!
# 4.Eng ko'p ovoz to'plagan nomzod!   5.Exit
# """)
#     a = int(input(">>>> "))
#     if a == 1:
#         for i in range(int(input("Nechta nomzod qo'shmoqchisiz: "))):
#             name = input("Ismini kiriting: ")
#             ovoz = int(input("Nechta ovozi bor: "))
#             word = f"{name}-{ovoz}"
#             user.add(word,name)
#     elif a == 2:
#         user.nomzodlar()
#     elif a == 3:
#         user.nomzodlarni_ochirish(input("Ismini kiriting: "))
#     elif a == 4:
#         user.kop_ovoz()
#     elif a == 5:
#         print("Sizni yana qaytip kuramiz degan umiddamiz!")
#         break
#     else:
#         print('Siz kiritgan buyruq boyicha malumot topilmadi!')


