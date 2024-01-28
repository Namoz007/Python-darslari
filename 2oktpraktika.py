#---------------------1------------------------
# with open("name.txt",'w+') as n:
#     while True:
#         name = input("Enter your name: ")
#         if name == 'stop':
#             break
#         else:
#             n.write(name)
#             n.write('\n')

#----------------------2----------------

# with open("name.txt",'w+') as n:
#     while True:
#         word = input("Enter your word: ")
#         if word == 'stop':
#             break
#         else:
#             n.write(word)
#             n.write(" ")
    
#     n.seek(0)
#     a = input("Enter --> ")
#     # words = n.read()
#     for i in n.read().split(" "):
#         if a in i:
#             print(i)



#---------------------3-----------------

# with open("male.txt") as n:
#     for i in n.read().split("\n"):
#         print(i.split(',')[0],end=" ")
#         print(i.split(',')[1],end=" ")
#         print(i.split(',')[4])


#------------------------4-----------------

# with open("malle.txt",'r',encoding="utf-8") as n:
#     n.seek(0)
#     for i in n.read().split("\n"):
#         a = i.split(',')[1]
#         if int(a) > 1000000:
#             print(i)

#------------------------5-----------------

# with open("cinema.txt") as c:
    # a = int(input("Vaqtni kirgizing: "))
    # for i in c.read().split('\n'):
    #     x = i.split(',')[5]
    #     if a == int(x.split(":")[0]):
    #         print(i)


    # l = input("Enter year: ")
    # for i in c.read().split("\n"):
    #     w = i.split(',')[3]
    #     b = i.split(",")[2]
    #     if int(l) > 2000:
    #         if 'Comedy' in i.split(",")[2] or 'Drama' in i.split(",")[2] or 'Romance' in i.split(",")[2]:
    #             print(i.split(',')[1] + '--' + i.split(',')[4])




    # for i in c.read().split("\n"):
    #     a = i.split(',')[5] 
    #     x = a.split(":")[0]
    #     if int(x) > 17:
    #         print(i)


#----------------------------6------------------

# with open("cinema.txt") as c:


    # for i in c.read().split("\n"):
    #     x = i.split(',')[3]
    #     if float(x.split('$')[1]) > 500 and float(x.split('$')[1]) < 1000:
    #         print(f"{i.split(',')[0]} -- {i.split(',')[2]}")


    # lst = []
    # a = input(">>>> ")
    # for i in c.read().split("\n"):
    #     if i.split(',')[2] == a and i.split(",")[4] == "true":
    #         lst.append(float(i.split(',')[3].split("$")[1]))
    # # lst.sort()
    # print(sorted(lst))



    # for i in c.read().split("\n"):
    #     if i.split(",")[4] == 'false' and float(i.split(',')[3].split("$")[1]) < 1000:
    #         print(i.split(',')[2])


#------------------------7-------------------------
# son = int(input('Nechta qiymat kiritasiz: '))
# while son > 0:
#     name = input("Enter your name: ")
#     firstname = input("Enter your first name: ")
#     number = int(input("Enter your number: "))
#     age = int(input("Enter your age: "))
#     locat = input("Enter your location: ")
#     with open(f"{name}{age}.txt","w+") as x:
#         x.write(f"Name:{name}")
#         x.write("\n")
#         x.write(f"Firstname:{firstname}")
#         x.write("\n")
#         x.write(f"Number:{number}")
#         x.write("\n")
#         x.write(f"Age:{age}")
#         x.write("\n")
#         x.write(f"Location:{locat}")
#         x.write("\n")
#     with open('allusers.txt','w+') as al:
#         al.write(f"{name}{age}.txt")
#         al.write("\n")
#     son -= 1
# lst = []
# with open("allusers.txt",encoding="utf-8") as all:
#     for i in all.readlines():
#         dct = {}
#         with open(i.split('\n')[0]) as fl:
#             for i in fl.readlines():
#                 flkey = i.split(":")[0]
#                 flvalue = i.split(":")[1]
#                 dct.update({flkey:flvalue})

#     lst.append(dct)
#     print(lst)


#------------------------9-------------

