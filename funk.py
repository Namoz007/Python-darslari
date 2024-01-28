# def dct(d1 : dict,d2 : dict):
#     for i,v in d1.items():
#         if i in d2:
#             d2[i] += v
#         else:
#             d2.update({i:v})
#     print(d2)

# d1 = {
#     'a' :  100,
#     'b' : 200,
#     'c' : 300
# }

# d2 = {
#     'a' :  300,
#     'b' : 200,
#     'd' : 400
# }


# dct(d1,d2)


# def dct(word: str):
#     dct = {}
#     for i in word:
#         count = word.count(i)
#         dct.update({i:count})
#     return  dct


# word = str(input('Biror bir soz kiriting: '))
# natija = dct(word)
# print(natija)




# def son(a: int):
#     b = str(a)
#     a = int(b[::-1])
#     return a

# a = int(input("biror bir son kiriting: "))
# natija = son(a)
# print(natija)




# def son(a: int):
#     b = str(a)
#     b = b[::-1]
#     print(b)
#     if str(a) == b:
#         return "palindrom"
#     return 'palindrommas'

# a = int(input("biror bir son kiriting: "))
# natija = son(a)
# print(natija)



# def son(a: int,b: int):
#     a = str(a)
#     b = str(b)
#     c = a + b
#     return int(c)


# a = int(input("chap tarafga qushish uchun bir son kiriting: "))
# b = int(input("Biror bir son kiriting: "))
# natija = son(a,b)
# print(natija)


# def soz(gap:str):
#     yangi = str()
#     a = input("biror bir soz kiriting: ")
#     b = input("biror bir soz kiriting: ")
#     c = input("biror bir soz kiriting: ")
#     for i in gap.split(" "):
#         if i in a or i in b or i in c:
#             for j in i:
#                 yangi += '*'
#         else:
#             yangi += i
#         yangi += ' '
#     return yangi

# gap = input("Biror bir gap kiriting: ")
# natija = soz(gap)
# print(natija)





# def son(yangi: int):
#     a = str(yangi)
#     for i in range(len(a)):
#         x = a[i]
#         a.removeprefix(a[i])
#         a+= x
#         print(a)


# yangi = int(input(">>>> "))
# natija = son(yangi)
# print(natija)




