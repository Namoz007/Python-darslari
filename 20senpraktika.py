#1

# lst = [True,54,65.5]

# for i in lst:
#     a = lst.index(i)
#     b = type(i)
#     lst.remove(i)
#     lst.insert(a,b)
# print(lst)


#2

# lst1 = [1,2,3,4,5,6,7,8,9]
# lst2 = []

# for i,v in  enumerate(lst1):
#     if i % 2 == 0:
#         lst2.append(v**2)
#     else:
#         lst2.append(v**3)
# print(lst2)


#3

# lst = [1,5,9,0,0,0,2,3,5,2,0,0,0,0,0]

# for i in lst:
#     if i == 0:
#         lst.append(0)
#         lst.remove(0)

# print(lst)


#4

# lst = [[1,6,5],[5,6,7],[8,9,2]]

# for i,v in enumerate(lst):
#     for j,k in enumerate(lst):
#         if lst[i][j] % 2 == 1:
#             lst[i][j] *= lst[i][j]
# print(lst)


#5

# lst = [[5,6,7],[8,6,7],[8,5,6]]
# qiymat = 0
# count = 0
# ind = 0
# for i,v in enumerate(lst):
#     for j,k in enumerate(lst):
#         qiymat += lst[i][j]
#     if qiymat > count:
#         count = qiymat
#         ind = i
#     qiymat = 0
# print(lst[ind])
# print(count)
    


#6

# lst1 = [1,6,8,3,6,7,9]
# lst2 = [6,8,2,9,4,3]
# lst3 = []

# for i in lst1:
#     for j in lst2:
#         if i == j and lst3.count(i) == 0:
#             lst3.append(i)
    
# print(lst3)


#7

# lst = [10,20,[100,400,[5000,6000],400,200],40,20]
# lst[2][2].append(7000)
# print(lst)


#8
# lst = []
# a = int(input("NEchta element kiritmoqchisan: "))
# while a:
#     num = int(input("Son kiriting: "))
#     if num != 0:
#         lst.append(num)
#     a -= 1

# lst.remove(max(lst))
# count = max(lst)
# print(count)


#9

# lst = [11,22,33]
# a = ""
# for i in lst:
#     a += str(i)
# print(a)


#10  

# a = [input("Biror bir soz kiriting: ")]
# for i in a:
#     if i == i[::-1]:
#         print("Palindrom.")
#     else:
#         print("Palindrom emas.")



#11

# lst = ['123',"lala","hsk","aba"]
# x = len(lst)

# for v,i in enumerate(lst):
#     if len(i) > 2 and i[0] == i[-1]:
#         print(v)

    
#12


