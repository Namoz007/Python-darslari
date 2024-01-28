
# class lst(list):
#     def remove(self, qiymat) -> None:
#         a = self.count(qiymat)     
#         count = 0
#         if qiymat in self:
#             while True:
#                 if count == a:
#                     break
#                 else:
#                     super().remove(qiymat)
#                     count += 1
#         else:
#             print("bunaqa qiymat mavjud emas.")

#     def appendd(self, indeks: int,qiymat: int) -> None:
#         if len(self) > indeks:
#             self.insert(indeks,qiymat)
#         else:
#             print("Bunaqa indeks mavjud emas.")
    
#     def qoshish(self,indeks,qiymat):
#         new_lst = self[indeks::]
#         new_lst2 = self[:indeks:]
#         new_lst2.append(qiymat)
#         for i in new_lst:
#             new_lst2.append(i)
#         print(new_lst2)
# a = lst((2,5,6,7,4,8,5,9,1,2,4,5,2,2,3,5,4,5))
# # a.remove(int(input(">>>> ")))
# # a.appendd(int(input("Indesks: ")),int(input("Qiymat kiriting: ")))
# a.qoshish(int(input("Indeks: ")),int(input("Qiymat: ")))
#---------------------------Masala-----------------------------
#------------------------1-masala------------------------------
class book:
        def __init__(self,id,name,author,count,price,balance) -> None:
                self.id = id
                self.name = name
                self.author = author
                self.count = count
                self.price = price
                self.buys = list()
                self.balans = balance

        def setNewBook(self):
            with open("kitoblar.txt",'a+') as f:
                f.seek(0)
                f.write(f"{self.id},{self.name},{self.author},{self.price},{self.count},\n")
        
        def getBuyBook(self):
            with open("kitoblar.txt") as f:
                for i in f.read().split("\n"):
                    book_id = i.split(",")[0]
                    book_name = i.split(",")[1]
                    book_author = i.split(",")[2]
                    book_price = i.split(",")[3]
                    book_count = i.split(",")[4]
                    print(f"Kitob nomi: {book_name}\nKitob muallifi: {book_author}\nKitob narxi: {book_price}\nKitob nusxasi: {book_count} ta\nKitob id: {book_id}")
            
            buy = int(input("Sotip olmoqchi bo'lgan kitob id: "))
            with open("kitoblar.txt") as f:
                for i in f.read().split("\n"):
                    j = i.split(",")[3]
                    if j == buy and self.balans > i.split(",")[3]:
                        self.buys.append(i.split(",")[1])
                        print("Kitob sotip olindi.")
                        break
    

    
while True:
    choise = input("Sotuvchi -->\nOluvchi  -->")
    if choise.lower == 'sotuvchi':
        user = book(int(input("Id kiriting: ")),input("Kitob nomini kiriting: "),input("Kitob muallifini kiriting: "),int(input("Kitobni nechta nusxasi bor: ")),int(input("Kitob narxi qancha: ")))
        while True:
            print(f"""
1.
""")
    elif choise.lower() == 'user':
        pass
    else:
        print("Siz no tog'ri malumot kiritdingiz.")
