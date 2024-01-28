import random

#masalalar

#1
# a = int(input("Birinchi raqamini kiriting: "))
# b = int(input("Ikkkinchi raqamini kiriting: "))
# c = int(input("Uchinchi raqamini kiriting: "))

# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > a and c > b:
#     print(c)



#2

# a = input("Biror bir soz kiriting: ")
# c = a[::-1]
# if a == c:
#     print("Palindrom")
# else:
#     print("Palindrom emas")


#3
# a = input("Biror bir soz kiriting: ")
# b = input("Biror bir soz kiriting: ")

# if len(a) % 2 == 0 and len(b) % 2 == 0:
#     print("True")
# else:
#     print("False")



#4

# a = int(input("Biror bir son kiriting: "))
# if a % 5 == 0 and a % 3 == 0:
#     print("FizzBuzz")
# elif a % 5 == 0:
#     print("Fizz")
# elif a % 3 == 0:
#     print("Buzz")
# else:
#     print("Not Fiz and not Buz")


#5  
# a = "salom bolalar salom"
# b = input("Qasyi sozni qidirmoqchisiz: ")
# c = a.count(b)

# if c % 2 == 0:
#     print(a[::-1])
# elif c == 1:
#     print(a.title())



# while


#1

# a = int(input("biror bir son kiriting: "))
# b = 1
# while b <= a:
#     print("* " * b)
#     b+=1


#2

# a = input("Biror bir soz kiriting: ")
# i = 0
# son = 0
# harf = 0

# while(i < len(a)):
#     if a[i].isalpha():
#         harf += 1
#     elif a[i].isdigit():
#         son += 1
#     i += 1

# print(f"{harf} ta harf bor\n{son} ta son bor")



#3
# nterms = int(input("How many terms? "))

# n1, n2 = 0, 1
# count = 0
# print("Fibonacci sequence:")
# while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

# print(n1)

#4

# a = int(input("Biror bir son kiriting: "))
# i = 2
# count = 0

# while i < a:
#     if a % i == 0:
#         count += 1
    
#     i += 1

# if count == 0:
#     print("Bu tup son")
# else:
#     print("Bu tup son emas")




# nterms = int(input("How many terms? "))

# n1, n2 = 0, 1
# count = 0
# print("Fibonacci sequence:")
# while count <  nterms- 1:
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1

# print(n1)



#for in range(start,stop,step):



# a = input("Biror bir son kiriting: ")
# c = int()
# f = 1
# for i in a:
#     i = int(i)
#     c += i *f
#     f *= 10

# a = int(a)
# print(a+ c)




# a = input("Biror bir soz kiriting: ")
# n = int(input("element raqami: "))
# z = str()

# y = a[:n-1:1]
# y += a[n::]
# print(y)






