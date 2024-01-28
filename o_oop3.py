# class karta:
#     def __init__(self,karta: str,bank_nomi: str,muddati: int,balans: int,karta_raqami: int,karta_pin: int) -> None:
#         self.karta = karta
#         self.bnom = bank_nomi
#         self.muddat = muddati
#         self.__balans = balans
#         self.__karta_pin = karta_pin
#         self.karta_raqam = karta_raqami
#     def getCardName(self):
#         print(self.karta)

#     def getCardNumber(self):
#         print(self.karta_raqam)

#     def getCardBank(self):
#         print(self.bnom)

#     def getDate(self):
#         print(self.muddat)

#     def getBalance(self):
#         print(self.__balans)

#     def setPin(self):
#         while True:
#             print("Iltimos eski parolni kiriting: ")
#             a = int(input(">>>> "))
#             x = str(a)
#             if a == self.__karta_pin and len(x) == 4:
#                 print("Yangi parolni kiriting: ")
#                 b = int(input(">>>> "))
#                 y = str(b)
#                 if len(y) == 4:
#                     print("Yangi parolni qaytadan kiriting: ")
#                     c = int(input(">>>> "))
#                     if b == c:
#                         self.__karta_pin = c
#                         break
#                     else:
#                         print("Siz boshqa boshqa parol kiritdingiz.")
#                 else:
#                     print("parolda kamida 4 raqam bo'lishi kerak.")
#             else:
#                 print("Siz kiritgan parol no to'gri.")

#     def setPul(self):
#         while True:
#             print("Kerakli summani kiriting. Summa kamida 1000 som bo'lishi shart.")
#             a = int(input(">>>> "))
#             if a >= 1000:
#                 print("Yubormoqchi bo'lgan karta raqamini yuboring.")
#                 b = int(input(">>>> "))
#                 if len(b) == 8:
#                     self.__balans -= a
#                     print(f"{b} kartaga {a} summa yuborildi.")
#                 else:
#                     print("Siz kiritgan karta umuman mavjud emas.")
#             else:
#                 print("Siz yuborgan summa kam.")
#     def kartapin(self):
#         print(self.__karta_pin)
# user = karta(input("Karta nomi: "),input("Bank nomi: "),int(input("Muddati: // yil ")),int(input("Balans: ")),int(input("Karta raqami: ")),int(input("Karta pin: ")))
# print(user.karta)
# while True:
#     print("1.Karta nomi.\n2.Karta olingan bank.\n3.Karta amal qilish muddati\n4.Balans\n5.Karta pin kodini o'zgartirish.\n6.Kartadan kartaga pul o'tqazish.\n7.Karta raqami.\n8.Karta pin.")
#     a = int(input(">>>> "))
#     if a == 1:
#         user.getCardName()
#     elif a == 2:
#         user.getCardBank()
#     elif a == 3:
#         user.getDate()
#     elif a == 4:
#         user.getBalance()
#     elif a == 5:
#         user.setPin()
#     elif a == 6:
#         user.setPul()
#     elif a == 7:
#         user.getCardNumber()
#     elif a == 8:
#         user.kartapin()
#     else:
#         print("Tugatildi.")
#         break
#------------------------------Masalalar---------------
#----------------------------1-masala--------------------
# class MinuteConventor:
#     def __init__(self,minute: int) -> None:
#         self.minute = minute

#     def toHours(self):
#         soat = self.minute // 60
#         minut = self.minute % 60
#         if minut == 0:
#             print(f"{self.minute} minut:{soat} soat bo'ladi.")
#         else:
#             print(f"{self.minute} minut: {soat} soat va {minut} minut bo'ladi.")

#     def toSeconds(self):
#         print(f"{self.minute * 60} sekund bo'ladi.")

#     def toDays(self):
#         soat = self.minute // 60
#         qold_min = self.minute % 60
#         kun = soat // 24
#         qold_soat = soat % 24
#         print(f"{kun} kun, {qold_soat} soat,{qold_min} minut qoldi.")
# user = MinuteConventor(int(input("Minut kiriting: ")))
# while True:
#     print("1.Soat\n2.Sekund\n3.Kunlar")
#     a = int(input(">>>> "))
#     if a == 1:
#         user.toHours()
#     elif a == 2:
#         user.toSeconds()
#     elif a == 3:
#         user.toDays()
#     else:
#         break
#---------------------------2-masala---------------------------
# class SpaceAircraft:
#     def __init__(self,model: str,height: int,fuel: int) -> None:
#         self.model = model
#         self.height = height
#         self.fuel = fuel
#         self.landd = int()
#     def land(self):
#         self.landd = int(input("Masofani kiriting: "))
#     def launch(self):
#         if self.landd >= self.fuel:
#             print(f"{self.model}")
#             self.fuel -= self.landd
#         else:
#             print("NO fuel.")
# user = SpaceAircraft(input("Modelini kiriting: "),int(input("Raketa uzunligini kiriting: ")),int(input("Yoqilg'ini kiriting: ")))
# while True:
#     print("1.Land\n2.Launch")
#     a = int(input(">>>> "))
#     if a == 1:
#         user.land()
#     elif a == 2:
#         user.launch()
#     else:
#         print("tugadi.")
#         break
#---------------------------------------------------------