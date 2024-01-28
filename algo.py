#-----------------------------------1-masala----------------------------------------------
# shart---> 13-jumani topish
# import datetime
# def find(year_input,month_input,day_input):
#     year = int(year_input)
#     month = int(month_input)
#     if int(day_input) > 13:
#         month += 1
#     day = 13
#     while True:
#         if month >= 13:
#             month = 1
#             year += 1
        
#         date_find = datetime.date(year,month,day).weekday()
#         if date_find == 4:
#             return datetime.date(year,month,day)
#         month += 1 

# date_input = input("Enter you now date Year-Month-Day with format: ")
# day_input = date_input.split("-")[2]
# month_input = date_input.split("-")[1]
# year_input = date_input.split("-")[0]
# find_date = find(year_input,month_input,day_input)
# print(find_date)
#-------------------------------------3-masala---------------------------------------------
# right_hand_letter = "67yuhjnmikolp890-=[]'/.,"
# left_hand_letter = '1qaz2wsx3edc4rfv5tgb'
# right_hand = 0; left_hand = 0
# words = input("Enter you words: ")
# for i in words:
#     if i.lower() in right_hand_letter:
#         right_hand += 1
#     elif i.lower() in left_hand_letter:
#         left_hand += 1

# print(f"Right hand: {right_hand}\nLeft hand: {left_hand}")
#-------------------------------------4-masala--------------------------------------------
# class Kasr:
#     def __init__(self,surat_1: int,maxraj_1:int,surat_2:int,maxraj_2:int) -> None:
#         pass
    
#     def qoshish(self,surat1,maxraj1,surat2,maxraj2):
#         self.maxraj1 = maxraj1
#         self.surat1 = surat1
#         self.surat2 = surat2
#         self.maxraj2 = maxraj2
#         if self.maxraj1 == self.maxraj2:
#             surat = self.surat1 + self.surat2
#             if surat == self.maxraj1:
#                 print("Javob: 1")
#             elif surat > self.maxraj1:
#                 ortiqcha = surat // self.maxraj1
#                 surat = surat % self.maxraj1
#                 print(f"{ortiqcha} butun {surat} taqsim {self.maxraj1}")
#             elif surat < self.maxraj1:
#                 print(f"{surat} taqsim {self.maxraj1}")
#         elif self.maxraj1 != self.maxraj2:
#             if self.maxraj1 > self.maxraj2:
#                 maxraj_count = self.maxraj2
#                 while True:
#                     maxraj_count += self.maxraj2
#                     if maxraj_count % self.maxraj1 == 0:
#                         break
#                 maxraj1_uchun = maxraj_count / self.maxraj1
#                 maxraj2_uchun = maxraj_count / self.maxraj2
#                 self.surat1 *= maxraj1_uchun
#                 self.surat2 *= maxraj2_uchun
#                 self.surat1 += self.surat2
#                 self.maxraj1 = maxraj_count
#                 if self.surat1 == self.maxraj1:
#                     print("Javob: 1")
#                 elif self.surat1 > self.maxraj1:
#                     butun = self.surat1 // self.maxraj1
#                     self.surat1 = self.surat1 % self.maxraj1
#                     print(f"{int(butun)} butun {int(self.surat1)} taqsim {int(self.maxraj1)}")
#                 else:
#                     print(f"{int(self.surat1)} taqsim {int(self.maxraj1)}")
                

#             elif self.maxraj1 < self.maxraj2:
#                 maxraj_count = self.maxraj1
#                 while True:
#                     maxraj_count += self.maxraj1
#                     if maxraj_count % self.maxraj2 == 0:
#                         break
#                 maxraj1_uchun = maxraj_count / self.maxraj1
#                 maxraj2_uchun = maxraj_count / self.maxraj2
#                 self.surat1 *= maxraj1_uchun
#                 self.surat2 *= maxraj2_uchun
#                 self.surat1 += self.surat2
#                 self.maxraj1 = maxraj_count
#                 if self.surat1 == self.maxraj1:
#                     print("Javob: 1")
#                 elif self.surat1 > self.maxraj1:
#                     butun = self.surat1 // self.maxraj1
#                     self.surat1 = self.surat1 % self.maxraj1
#                     print(f"{int(butun)} butun {int(self.surat1)} taqsim {int(self.maxraj1)}")
#                 else:
#                     print(f"{self.surat1} taqsim {self.maxraj1}")

#     def ayirish(self,surat1,maxraj1,surat2,maxraj2):
#         self.maxraj1 = maxraj1
#         self.surat1 = surat1
#         self.surat2 = surat2
#         self.maxraj2 = maxraj2
#         if self.maxraj1 == self.maxraj2:
#             surat = self.surat1 - self.surat2
#             if surat == self.maxraj1:
#                 print("Javob: 1")
#             elif surat > self.maxraj1:
#                 ortiqcha = surat // self.maxraj1
#                 surat = surat % self.maxraj1
#                 print(f"{ortiqcha} butun {surat} taqsim {self.maxraj1}")
#             elif surat < self.maxraj1:
#                 print(f"{surat} taqsim {self.maxraj1}")
#         elif self.maxraj1 != self.maxraj2:
#             if self.maxraj1 > self.maxraj2:
#                 maxraj_count = self.maxraj2
#                 while True:
#                     maxraj_count += self.maxraj2
#                     if maxraj_count % self.maxraj1 == 0:
#                         break
#                 maxraj1_uchun = maxraj_count / self.maxraj1
#                 maxraj2_uchun = maxraj_count / self.maxraj2
#                 self.surat1 *= maxraj1_uchun
#                 self.surat2 *= maxraj2_uchun
#                 self.surat1 -= self.surat2
#                 self.maxraj1 = maxraj_count
#                 if self.surat1 == self.maxraj1:
#                     print("Javob: 1")
#                 elif self.surat1 > self.maxraj1:
#                     butun = self.surat1 // self.maxraj1
#                     self.surat1 = self.surat1 % self.maxraj1
#                     print(f"{int(butun)} butun {int(self.surat1)} taqsim {int(self.maxraj1)}")
#                 else:
#                     print(f"{int(self.surat1)} taqsim {int(self.maxraj1)}")
                

#             elif self.maxraj1 < self.maxraj2:
#                 maxraj_count = self.maxraj1
#                 while True:
#                     maxraj_count += self.maxraj1
#                     if maxraj_count % self.maxraj2 == 0:
#                         break
#                 maxraj1_uchun = maxraj_count / self.maxraj1
#                 maxraj2_uchun = maxraj_count / self.maxraj2
#                 self.surat1 *= maxraj1_uchun
#                 self.surat2 *= maxraj2_uchun
#                 self.surat1 -= self.surat2
#                 self.maxraj1 = maxraj_count
#                 if self.surat1 == self.maxraj1:
#                     print("Javob: 1")
#                 elif self.surat1 > self.maxraj1:
#                     butun = self.surat1 // self.maxraj1
#                     self.surat1 = self.surat1 % self.maxraj1
#                     print(f"{int(butun)} butun {int(self.surat1)} taqsim {int(self.maxraj1)}")
#                 else:
#                     print(f"{int(self.surat1)} taqsim {int(self.maxraj1)}")

#     def kupaytirish(self,surat1,maxraj1,surat2,maxraj2):
#         self.maxraj1 = maxraj1
#         self.surat1 = surat1
#         self.surat2 = surat2
#         self.maxraj2 = maxraj2
#         self.surat1 *= self.surat2
#         self.maxraj1 *= self.maxraj2
#         if self.surat1 == self.maxraj1:
#             print("Javob: 1")
#         elif self.surat1 < self.maxraj1:
#             asos = self.surat1 // 2
#             count = 0
#             while True:
#                 if asos == 1:
#                     break
#                 if self.surat1 % asos == 0 and self.maxraj1 % asos == 0:
#                     self.surat1 = self.surat1 // asos;self.maxraj1 = self.maxraj1 // asos
#                     print(f"{self.surat1} taqsim {self.maxraj1}")
#                     count += 1
#                     break
#                 asos -= 1
            
#             if count == 0:
#                 print(f"]{self.surat1} taqsim {self.maxraj1}")
#         elif self.surat1 > self.maxraj1:
#             butun = self.surat1 // self.maxraj1
#             self.surat1 = self.surat1 % self.maxraj1
#             asos = self.surat1 // 2
#             count = 0
#             while True:
#                 if asos == 1:
#                     break
#                 if self.surat1 % asos == 0 and self.maxraj1 % asos == 0:
#                     self.surat1 = self.surat1 // asos;self.maxraj1 = self.maxraj1 // asos
#                     print(f"{butun} butun {self.surat1} taqsim {self.maxraj1}")
#                     count += 1
#                     break
#                 asos -= 1
            
#             if count == 0:
#                 print(f"{butun} butun {self.surat1} taqsim {self.maxraj1}")

#     def bolish(self,surat1,maxraj1,surat2,maxraj2):
#         self.maxraj1 = maxraj1
#         self.surat1 = surat1
#         self.surat2 = surat2
#         self.maxraj2 = maxraj2
#         self.surat1 *= self.maxraj2
#         self.maxraj1 *= self.surat2
#         if self.surat1 == self.maxraj1:
#             print("Javob: 1")
#         elif self.surat1 < self.maxraj1:
#             asos = self.surat1 // 2
#             count = 0
#             while True:
#                 if asos == 1:
#                     break
#                 if self.surat1 % asos == 0 and self.maxraj1 % asos == 0:
#                     self.surat1 = self.surat1 // asos;self.maxraj1 = self.maxraj1 // asos
#                     print(f"{self.surat1} taqsim {self.maxraj1}")
#                     count += 1
#                     break
#                 asos -= 1
            
#             if count == 0:
#                 print(f"]{self.surat1} taqsim {self.maxraj1}")
#         elif self.surat1 > self.maxraj1:
#             butun = self.surat1 // self.maxraj1
#             self.surat1 = self.surat1 % self.maxraj1
#             asos = self.surat1 // 2
#             count = 0
#             while True:
#                 if asos == 1:
#                     break
#                 if self.surat1 % asos == 0 and self.maxraj1 % asos == 0:
#                     self.surat1 = self.surat1 // asos;self.maxraj1 = self.maxraj1 // asos
#                     print(f"{butun} butun {self.surat1} taqsim {self.maxraj1}")
#                     count += 1
#                     break
#                 asos -= 1
            
#             if count == 0:
#                 print(f"{butun} butun {self.surat1} taqsim {self.maxraj1}")

# surat1 = int(input("Birinchi kasr surati: "))
# maxraj1 = int(input("Birinchi kasr maxraji: "))
# surat2 = int(input("Ikkinchi kasr surati: "))
# maxraj2 = int(input("Ikkinchi kasr maxraji: "))
#Samandar aka man bulani alohida ozgaruvchiga olip oldim, sababi ozgaruvchilar ustida amal bajarganimizda ular ozgarip ketyapti
# user = Kasr(surat1, maxraj1, surat2, maxraj2)
# while True:
#     print("""
#     1.Kasrni qoshish            2.Kasrlarni ayirish
#     3.Kasrlarni kupaytirish     4.Kasrlarni bo'lish
#     5.Exit
#     """)
#     a = int(input(">>>> "))

#     if a == 1:
#         user.qoshish(surat1,maxraj1,surat2,maxraj2)
#     elif a == 2:
#         user.ayirish(surat1,maxraj1,surat2,maxraj2)
#     elif a == 3:
#         user.kupaytirish(surat1,maxraj1,surat2,maxraj2)
#     elif a == 4:
#         user.bolish(surat1,maxraj1,surat2,maxraj2)
#     elif a == 5:
#         print("Bizga vaqt ajratganingiz uchun rahmat!")
#         break
#     else:
#         print("Bunaqa buyruq mavjud emas!")
#----------------------------------7-masala-----------------------------------------------
# def analist(xaridor,xaridor_kup,sotuvchi_kup):
#     for i in xaridor_kup:
#         if i == xaridor:
#             return f"{xaridor}-{i}"    
#     count = 0
#     count_lst = list()
#     kup = list(xaridor_kup)
#     kup.sort(reverse=True)
#     for i in kup:
#         count += i
#         count_lst.append(i)
#         word = str()
#         if count == xaridor:
#             if len(count_lst) == 1:
#                 for i in count_lst:
#                     print(f"{i}-0")
#                     return 
#             else:
#                 one = count_lst[0]
#                 print(count_lst[0],end="")
#                 count_lst.remove(one)
#                 for i in count_lst:
#                     print('+',end="")
#                     print(i,end="")
#                 return
#         if count > xaridor:
#             count -= i
#             count_lst.remove(i)
#     count = 0
#     count_lst = list()
#     kup = list(xaridor_kup)
#     kup.sort(reverse=True)
#     for i in kup:
#         count += i
#         count_lst.append(i)
#         if count > xaridor:
#             orada = count - xaridor
#             for j in sotuvchi_kup:
#                 if j == orada:
#                     if len(count_lst) == 1:
#                         print(f"{count_lst}-0")
#                     else:
#                         one = count_lst[0]
#                         print(one,end="")
#                         count_lst.remove(one)
#                         for i in count_lst:
#                             print("+",end="")
#                             print(i,end="")
#                         print(f"-{j}")
#                         return
#             count -= i
#             count_lst.remove(i)  
#     kup = list(xaridor_kup)
#     kup.sort()
#     count = 0
#     count_lst = list()
#     sotuv = list(sotuvchi_kup)
#     sotuv.sort()
#     s_kup = 0
#     s_kup_lst = list()
#     for i in kup:
#         count += i
#         count_lst.append(i)
#         if count > xaridor:
#             orta = count - xaridor
#             for j in sotuv:
#                 s_kup += j
#                 s_kup_lst.append(j)
#                 if s_kup > orta:
#                     s_kup -= j
#                     s_kup_lst.remove(j)
#                 elif orta == s_kup:
#                     if len(s_kup_lst) == 1:
#                         one = count_lst[0]
#                         print(one,end="")
#                         count_lst.remove(one)
#                         for k in count_lst:
#                             print('+')
#                             print(k)
#                         print('-',s_kup_lst)
#                         return
#                     else:
#                         word = count_lst[0]
#                         print(word,end="")
#                         count_lst.remove(word)
#                         for z in count_lst:
#                             print('+',end="")
#                             print(z,end="")
#                         one = s_kup_lst[0]
#                         print(f"-{one}",end="")
#                         s_kup_lst.remove(one)
#                         for i in s_kup_lst:
#                             print('+',end='')
#                             print(i)
#                         return

#     print("Impossible!")

# xaridor = int(input("Necha sumlik tavar sotip olmoqchisiz: "))
# xaridor_kup = list()
# for i in range(int(input("Nechta kupyura bor: "))):
#     xaridor_kup.append(int(input("Necha sumlik kupyura bor: ")))

# sotuvchi_kup = list()
# for i in range(int(input("Sotuvchida nechta kupyura bor: "))):
#     sotuvchi_kup.append(int(input("Necha sumlik kupyura bor: ")))

# analist(xaridor,xaridor_kup,sotuvchi_kup)

#----------------------------------------------------------------------------------
