#1

# lst = [1,5,3,4,8,1,5,9,65,85,26,45]

# with open("juft.txt",'w+') as juft:
#     for i in lst:
#         if i % 2 == 0:
#             i = str(i)
#             juft.write(i + " ")
            


# with open("toq.txt",'w+') as toq:
#     for i in lst:
#         if i % 2 == 1:
#             i = str(i)
#             toq.write(i + " ")



#2     

# with open('email.txt') as f:
#     for i in f.read().split():
#         a = i[::-1]
#         for j in a.split("."):
#             print(j[::-1])
#             break




#3

# with open('email.txt') as f:
#     for i in f.read().split('\n'):
#         print(i[5:7:1])
        


#4

# lst = []
# lst2 = []
# count = 0
# with open('email.txt') as f:
#     for i in f.read().split('\n')[:-1]:
#         lst.append(i)
#         lst2.append(i.split()[1])
#     lst2.sort()
#     # print(lst2)
#     for i in lst2:
#         for j in lst:
#             if i in j:
#                 print(j)
#                 break
        

#5

    