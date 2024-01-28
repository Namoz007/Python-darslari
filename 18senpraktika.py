#7
# for i in range(1,141):
#     if i % 2 == 0:
#         print(i)


#8
# for i in range(100,240):
#     if i % 2 == 1:
#         print(i)


#9
# for i in range(50,140):
#     if i % 7 == 0:
#         print(i)

#10

# for i in range(50,140):
#     if i % 11 == 0:
#         print(i)

#10

# for i in range(90,210):
#     if i % 25 == 0:
#         print(i)


#11
# for i in range(25,690):
#     if i % 5 == 0:
#         print(i)
#     elif i % 9 == 0:
#         print(i)

#12

# for i in range(1,4000):
#     if i % 11 == 0:
#         print(i)
#     elif i % 3 == 0:
#         print(i)
#     elif i % 9 == 0:
#         print(i)






#keyingi masalalar

#P1
# mylist = [True,"Salom",5,5.6]

# for i in mylist:
#     print(type(i))




#P2

# mylist = [7,8,1,3,4,6,7,5]

# count = 0
# for i in mylist:
#     if i % 2 == 0:
#         mylist[count] = i ** 2
#     else:
#         mylist[count] = i ** 3
#     count += 1

# print(mylist)




#P3         bajarilmadi

# mylist = [0,0,0,0,0,0,0,0,6,4,2,8,9,7,8]
# numlist = []


# numb = []
# ind = 0
# count = 0
# for i in mylist:
#     if i == 0:
#         numb[ind] = count
#         ind += 1
#     count += 1
# print(numb)
        


#P9

# mylist = []
# a = int(input("Listga nechta element bermoqchisiz: "))

# for i in range(a):
#     mylist.append(int(input("Qiymatni kiriting: ")))

# mylist.sort()
# mylist.reverse()


# for i in range(0,len(mylist)):
#     if mylist[i] != mylist[i+1] and mylist[i + 1] != mylist[i + 2]:
#         print(mylist[i+1])
#         break



#P10                    bajarilmadi

# mylist = [1,2,3,4,8,6,78,4,52,4,6]
# mylist.sort()
# for i in mylist:
#     count = 0
#     for x in mylist:
#         if i == x:
#             count += 1

#         if count == 1:
#             print(i)



#P11
# myist = [11,33,50]

# for i in myist:
#     print(i,end="")


#P12

# list1 = [1,2,3,4,5,6,7,8]
# list2 = [1,2,3,4,4,5,6,7,8]
# a = len(list1) + len(list2)

# count = int()
# for i in list1:
#     count += i

# for i in list2:
#     count += i

# print(count // a)

