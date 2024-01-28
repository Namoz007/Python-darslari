a = int(input(">>>> "))
for i in range(a):
    for j in range(a):
        if i + j == a - 1 or i == j:
            print(1,end=" ")
        else:
            print(0,end=" ")

    print()



# word = input(">>>> ")
# for i in word.upper():
#     if i == 'A':
#         print("x",end="")
#     elif i == 'B':
#         print("y",end="")
#     elif i == 'C':
#         print("z",end="")
#     elif i == 'D':
#         print("a",end="")
#     elif i == 'Q':
#         print("n",end="")
#     elif i == 'W':
#         print("t",end="")
#     elif i == 'E':
#         print("b",end="")
#     elif i == 'R':
#         print("o",end="")
#     elif i == 'T':
#         print("q",end="")
#     elif i == 'Y':
#         print("v",end="")
#     elif i == 'U':
#         print("r",end="")
#     elif i == 'I':
#         print("f",end="")
#     elif i == 'O':
#         print("l",end="")
#     elif i == 'P':
#         print("m",end="")
#     elif i == 'S':
#         print("p",end="")
#     elif i == 'F':
#         print("c",end="")
#     elif i == 'G':
#         print("d",end="")
#     elif i == 'H':
#         print("e",end="")
#     elif i == 'J':
#         print("g",end="")
#     elif i == 'K':
#         print("h",end="")
#     elif i == 'Z':
#         print("w",end="")
#     elif i == 'X':
#         print("u",end="")
#     elif i == 'V':
#         print("s",end="")
#     elif i == 'N':
#         print("k",end="")
#     elif i == 'M':
#         print("j",end="")

# user = input(">>>> ")
# lst = []
# if user.isspace():
#     pass
# else:
#     for i in user.split(" "):
#         lst.append(i)
# while True:
#     if len(lst) == 0:
#         print("no one like this!")
#         break
#     elif len(lst) == 1:
#         for i in lst:
#             print(f"{i} like this!")
#         break
#     elif len(lst) == 2:
#         print(lst[0],end=" and ")
#         print(lst[1],end=' like this!')
#         break
#     else: 
#         a = lst[0]
#         print(a,end="")
#         lst.remove(a)
#         for i in lst:
#             print(',',end="")
#             print(i,end='')
#         print(" like this")
#         break


# def case(word:str):
#     if '_' in word:
#         new = ""
#         count = word.count("_")
#         a = 0
#         for i in word.split("_"):
#             if a == 0:
#                 new += i
#             else:
#                 x = 0
#                 for j in i:
#                     if x == 0:
#                         new += (j.upper())
#                     else:
#                         new += j
#                     x+= 1
#             a+= 1
#         return new
#     else:
#         new = ''
#         for i in word:
#             if i.isupper():
#                 new+= f"_{i.lower()}"
#             else:
#                 new += i
#         return new


# word = input(">>>> ")
# print(case(word))



# A = 'bchig'
# D = 'klnmo'
# F = 'qprst'
# G = 'uvwxy'
# X = 'zadef'

# word = input(">>>> ")
# for i in word.lower():
#     if i in A:
#         print("A",end="")
#     elif i in D:
#         print("D",end="")
#     elif i in F:
#         print('F',end="")
#     elif i in G:
#         print("G",end="")
#     elif i in X:
#         print("X",end="")