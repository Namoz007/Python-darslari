#------------1-masala
# k = int(input('Nechta keygli bor: '))
# n = int(input("Necha marta urinish bo'lgan: "))
# urilgan = []
# for i in range(n):
#     a = input(">>>> ")
#     for j in a.split(" "):
#         urilgan.append(int(j))
# keygli = [];count = 1
# for i in range(k):
#     if count in urilgan:
#         keygli.append("*")
#     else:
#         keygli.append(count)
#     count += 1
# qatlam = 1;lst = []
# for i in keygli:
#     lst.append(i)
#     print(i,end=" ")
#     if len(lst) == qatlam:
#         qatlam += 1
#         lst = []
#         print()

#------------2-masala--

#-----------3-masala---
# input_word = input("Enter you words: ")
# new_word = ''
# for i in input_word:
#     if i.isalpha() or i.isdigit() or i == "\\" or i == ',' or i == '!':
#         new_word += f"{i}"
#     elif i.isspace():
#         new_word += ' '
# word = ''
# for i in new_word.split(" "):
#     if i == 'or' or i == 'and':
#         pass
#     else:
#         word += i
#     word += ' '
# print(word)
#---------------4-masala--
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


# from random import choice   
# colors = []
# for i in range(int(input("Necha xil rang bor: "))):
#     colors.append(input("qanaqa rang bor: "))
# count = 0;boyalganlar = colors[0]
# count = 0
# for i in colors:
#     if i == boyalganlar:
#         count += 2
#         boyalganlar = i
#     else:
#         count += 1
#         boyalganlar = i
#         count += 2
# print(count)


# number = input("Faqat 0 6 9 raqamlardan tashkil topgan son kiriting: ")
# new_number = ''
# for i in number:
#     if i =='6':
#         new_number += '9'
#     elif i == '9':
#         new_number += '6'
#     else:
#         new_number+= '0'
# if new_number[::-1] == number:
#     print(True)
# else:
#     print(False)



# phone_number = input("Telefon raqamingizni kiriting: Masalan->(998) 99-999-99-99: ")
# count = 0
# if phone_number.split(" ")[0] == '(998)':
#     new_number = phone_number.split(" ")[1]
#     one = new_number.split("-")[0]
#     two = new_number.split("-")[1]
#     three = new_number.split('-')[2]
#     four = new_number.split("-")[3]
#     if len(one) == 2 and len(two) == 3 and len(three) == 2 and len(four) == 2 and new_number.count('-') == 3:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)



# name = input("Enter you name: ")
# age = int(input("Enter you age: "))
# if age % 2 == 0:
#     happy = f"# {age} Happy Birthday {name}! {age} #"
#     ramka = ''
#     for i in range(len(happy)):
#         ramka += '#'
#     print(ramka)
#     print(happy)
#     print(ramka)
# else:
#     happy = f"* {age} Happy Birthday {name}! {age} *"
#     ramka = ''
#     for i in range(len(happy)):
#         ramka += '*'
#     print(ramka)
#     print(happy)
#     print(ramka)




# import mysql.connector
# db = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'muhammadzohid2007@'
# )
# cursor = db.cursor()
# cursor.execute('use user;')
# cursor.execute("select * from user;")
# result = cursor.fetchall()

#turmush qurgan
# address = [];address_s = [];familys = []
# for i in result:
#     a = list(i)
#     if a[4] not in address:
#         address.append(a[4])
#     address_s.append(a[4])
# for i in address:
#     count = 0
#     for j in address_s:
#         if i == j:
#             count += 1
#     if count == 2:
#         new = (f"select * from user where address = '{i}';")
#         cursor.execute(new)
#         familys.append(cursor.fetchall())
# for i in familys:
#     for j in i:
#         a = i[0]
#         b = i[1]
#         print(f"{a[1]} {a[2]} bilan {b[1]} {b[2]} bir oila.Ular {a[4]} tumanida yashashadi,{a[1]} {a[2]} {a[3]} yoshda va {b[1]} {b[2]} {b[3]} yoshda.")
#         print()
#         break

#turmush qurmagan
# address = [];address_s = [];familys = []
# for i in result:
#     a = list(i)
#     if a[4] not in address:
#         address.append(a[4])
#     address_s.append(a[4])
# new_add = []
# for i in address:
#     count = 0
#     for j in address_s:
#         if i == j:
#             count += 1
#     if count == 1:
#         new_add.append(i)
# for i in new_add:
#     new = (f"select * from user where address = '{i}';")
#     cursor.execute(new)
#     familys.append(cursor.fetchall())
# for i in familys:
#     a = i[0]
#     print(f"{a[1]} {a[2]} oila qurmagan.U {a[4]} tumanida yashaydi,{a[1]} {a[2]} {a[3]} yoshda.")
#     print()




# animals = ['dog','cat','bat','cock','cow','pig','fox','ant','bird','lion','wolf','deer','bear','frog','hen','mole','duck','goat']
# word = input("Enter you animals name: ")
# word_animals = []; count_animals = []
# for i in word:
#     word_animals.append(i)
# for x in range(len(animals)):
#     for i in animals:
#         new_animal = ''
#         for j in i:
#             if j in word_animals:
#                 new_animal += j
#         if new_animal in animals and new_animal not in count_animals:
#             count_animals.append(new_animal)
#             # print(new_animal)
# print(count_animals)



# arena = [    #bajarilmadi
#     [0,1,1,1,1,0,0],
#     [0,0,0,0,1,0,0],
#     [1,1,1,0,0,0,0],
#     [1,0,0,0,1,1,0],
#     [1,1,1,1,1,0,0]
# ]
# onee = arena[0]
# twoo = arena[-1]
# count = 0; end = 0;ind = 0;qatlam = 0
# if onee[0] == 0 and twoo[-1] == 0:
#     while True:
#         if qatlam == 6:
#             break

#         if qatlam != 0:
#             if ind > 0:
#                 one = ind-1
#                 two = ind
#                 three = ind + 1
#                 if arena[qatlam][three] == 0:
#                     ind =  three
#                     qatlam += 1
#                     print(qatlam-1,ind)
#                 elif arena[qatlam][two] == 0:
#                     ind = two
#                     qatlam += 1
#                     print(qatlam-1,ind)
#                 elif arena[qatlam][one] == 0:
#                     ind = one
#                     qatlam += 1
#                     print(qatlam-1,ind)
#                 elif arena[qatlam-1][ind+1] == 0:
#                     ind += 1
#                     print(qatlam-1,ind)
#                 elif arena[qatlam-2][ind+1] == 0:
#                     ind += 1
#                     qatlam -= 1
#                     print(qatlam-2,ind)
#                 elif arena[qatlam-2][ind] == 0:
#                     qatlam -= 1
#                     print(qatlam-2,ind)
#                 else:
#                     print(False)
#                     end += 1
#                     break
#             else:
#                 one = ind
#                 two = ind + 1
#                 if arena[qatlam][two] == 0:
#                     ind = two
#                     qatlam += 1
#                     print(qatlam-1,ind)
#                 elif arena[qatlam][one] == 0:
#                     ind = one
#                     qatlam += 1
#                     print(qatlam-1,ind)
#                 elif arena[qatlam-1][ind+1] == 0:
#                     ind += 1
#                     print(qatlam-1,ind)
#                 elif arena[qatlam-2][ind+1] == 0:
#                     ind += 1
#                     qatlam -= 1
#                     print(qatlam-2,ind)
#                 elif arena[qatlam-2][ind] == 0:
#                     qatlam -= 1
#                     print(qatlam-2,ind)
#                 else:
#                     print(False)
#                     end += 1
#                     break
#         else:
#             qatlam += 1
#     if end == 0:
#         print(True)

# else:
#     print(False)



# a = int(input(">>> "))
# for i in range(a):
#     for j in range(a):
#         if i == j or i + j == a - 1:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()





# a = input(">>> ")
# lst = []
# for i in a.split(" "):
#     if i not in lst:
#         lst.append(i)
#         print('NO',end=" ")
#     else:
#         print("YES",end=" ")




# lst = [
#     [1,1,1,1,1],
#     [0,0,0,0,0],
#     [0,0,1,1,0],
#     [1,0,0,1,1]
# ]
# islands = 0
# for i in lst:
    