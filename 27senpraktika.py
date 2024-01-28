#1

# def sonlar(a: int):
#     b = str(a)
#     return len(b)

# a = int(input("Biror bir son kiriting: "))
# natija = sonlar(a)
# print(natija)




#2

# def tortburchak(en: int,boy: int):
#     new = set()
#     eni = (en * 2) + (boy * 2)
#     boy = en * boy
#     new.add(eni)
#     new.add(boy)
#     return new

# en = int(input("tortburchak enini kiriting: "))
# boy = int(input("tortburchak boyini kiriting: "))

# natija = tortburchak(en,boy)
# print(natija)



#3

# def project(max: int,min: int):
#     if max == min:
#         return min
#     print(max,end=" ")
#     return project(max-1,min)

# max = int(input("Max sonni kiriting: "))
# min = int(input("Min sonni kiriting: "))

# natija = project(max,min)
# print(natija)


#5

# def hisoblash(tpl: tuple):
#     lst = []
#     for i in tpl:
#         count = 0
#         for j in i:
#             count += j
#         lst.append(count)
#     return lst

# tpl = ((1,2),(3,4),(5,6))
# natija = hisoblash(tpl)
# print(natija)


#6

# def lstga(tpl: tuple):
#     newtpl = list()
#     for i in tpl:
#         a = list(i)
#         newtpl.append(a)
#     return newtpl

# tpl = ((1,2,3),(4,5,6),(9,7,5))
# natija = lstga(tpl)
# print(natija)


#7

# def myFunction(lst1:list, lst2: list, lst3:list): 
#     result = dict.fromkeys (lst1)
#     index = 0
#     lst2.extend(lst3)
#     for i in lst1:
#         result[i] = {lst2[index]:lst2[index+len(lst3)]}
#         index += 1
#     print(result)

# lst1 = ['S001','S002','S003','S004']
# lst2 = ['Adina Park','Leyton Marsh','Duncan Boyle', 'Saim Richards']
# lst3 = [85,98,89,92]
# natija = myFunction(lst1,lst2,lst3)

#8



#9

# def listochish(lst: list):
#     for i in lst:
#         for j in i:
#             if isinstance(j,int):
#                 i.remove(j)
#     dct = {}
#     for i in lst:
#         i = str(i)

#     for i in range(len(lst)):
#         dct.update({i+1:lst[i]})
#     return dct

# lst = [
#     [1,'Jean','V'],
#     [2,'Lara','V'],
#     [3,'JOhn','VI'],
#     [4,'Nuke','IV'],
#     [5,'Jallol','VII']
# ]

# natija = listochish(lst)
# print(natija)



#10





#11


#cars papkasida



#12


