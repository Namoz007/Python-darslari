#-------------------------1-------------------------------
# def data(a,b,c):
#     print(a,end=".")
#     if b == 1:
#         print("Yanvar",end=".")
#     elif b == 2:
#         print("Fevral",end=".")
#     elif b == 3:
#         print("Mart",end=".")
#     elif b == 4:
#         print("Aprel",end=".")
#     elif b == 5:
#         print("May",end=".")
#     elif b == 6:
#         print("Iyun",end=".")
#     elif b == 7:
#         print("IYul",end=".")
#     elif b == 8:
#         print("Avgust",end=".")
#     elif b == 9:
#         print("Sentabr",end=".")
#     elif b == 10:
#         print("Okatabr",end=".")
#     elif b == 11:
#         print("Noyabr",end=".")
#     elif b == 12:
#         print("Dekabr",end=".")
    
#     print(f"{c}-yil")
        

#-----------------------------2-------------------

# def top(a):
#     count = 0
#     for i in a:
#         if i == '0':
#             count += 1
#         else:
#             break
#     print(count)



#----------------------------3-------------------

# def azbuka(a: str):
#     dct = {
#         '-----' :  0,
#         '.----' : 1,
#         "..---" : 2,
#         "...--" : 3,
#         "....--" : 4,
#         "....." : 5,
#         "-...." : 6,
#         "--..." : 7,
#         "---.." : 8,
#         "----." : 9
#     }

#     for i in a.split(" "):
#         print(dct[i],end="")
        


#----------------------------4-----------------         bajarilmadi
# def kesish(a):
#     lst = ['A','B','C','D','E','F','G','H','I','J']
#     lst1 = []
#     lst2 = []
#     count = 0
#     ind = a
#     lst_ind = 0
#     for i in range(len(lst)):
#         if count < ind:
#             lst2.append(lst[lst_ind])
#         elif count == ind:
#             lst1.append(lst2)
#             ind = 0
#             count = -1
#         # if count >= a:
#         #     lst2.append(lst[count])
#         count += 1
#         lst_ind += 1
#     print(lst1)



#-------------------------5--------------

# def sort(lst: list):
#     dct = {}
#     for i in lst:
#         if i not in dct:
#             count = 0
#             for j in lst:   
#                 if i == j:
#                     count += 1
#             dct.update({i:count})
#     print(dct)

#------------------------6---------

