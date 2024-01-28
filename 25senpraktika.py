#1

# st1 = {"sariq",'yashil','qizil','oq'}
# st2 = ['yashil','qora','oq','pushti']
# c = st1.union(st2)
# print(c)



#2

# st1 = {10,20,30,50,60}
# st2 = {10,20,35,40,60}
# c = st1.intersection(st2)
# print(st1)

#3

# st1 = {10,20,30,50,60}
# st2 = {10,20,35,40,60}
# c = st1.symmetric_difference(st2)
# print(c)


#4
# sett = [set(),set()]

# ind = 0
# count = 1
# while True:
#     sett[ind].add(input(">>>> "))
#     if len(sett[0]) < count:
#         ind += 1
#         count = 1
    
#     if ind == 2:
#         break
    
#     # sett[ind].add(a)
#     count += 1

# # print(sett[0].intersection(sett[1]))
# # print()
# # print(sett[0].difference(sett[1]))

# print(sett[0])
# print(sett[1])


#5

# n = int(input("Nechta son kiritasiz: "))
# max = int(input("Max sonni kiriting: "))
# min = int(input("Min sonni kiriting: "))
# sett = set()
# lst = list()
# for i in range(n):
#     a = int(input("Sonni kiriting: "))
#     if a > max or a < min:
#         lst.append(a)
    
#     if a > min and a < max:
#         sett.add(a)

# print(sett)
# print(lst)



#5 

# dct = {'a' : 100, 'b' : 200,'c' : 300}
# count = 0
# for v in dct.values():
#     if v == 200:
#         count += 1
# if count > 0:
#     print('bor')
# else:
#     print('yoq')


#6

# dct = {
#     'name' : 'Keliy',
#     'age' :  25,
#     'salary' : 80000,
#     'city' : 'New york'
# }

# a = dct['city']
# dct.pop('city')
# dct.update({'location':a})
# print(dct)



#7

# word = str(input('Biror bir soz kiriting: '))
# dct = {}
# for i in word:
#     count = word.count(i)
#     dct.update({i:count})
# print(dct)


#8
# ind = 1
# dct = {}
# while True:
#     a = input(">>>> ")
#     if a == 'stop':
#         break
#     dct.setdefault(ind,a)
#     ind += 1
# print(dct)