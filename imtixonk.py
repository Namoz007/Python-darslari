#-----------------------1-masala--------------
# a = int(input('4 dan katta bolgan son kiriting:  '))
# count = 1
# for i in range(a):
#     for j in range(a):
#         if i == 0 or i == a-count or j == a - count or (i !=  1 and j == 0) or (i - j) % 2 == 0:
#             print(1,end=" ") 
#         else:
#             print(0,end=" ")
#     print()
#-----------------------2-masala--------------
# a = int(input("enter you number: "))
# n = 0;ind = 0;s = 0
# while ind < a:
#     s += n
#     n += 5
#     ind += 1
# s += 1
# print(s)
#-----------------------3-masala--------------
# with open("input.txt") as f:
#     words = f.read()
#     words_lst = []
#     for i in words:
#         if i not in words_lst:
#             words_lst.append(i)
#         else:
#             words_lst.append('*')
# input_word = "".join(map(str,words_lst))
# with open('output.txt','w') as f:
#     f.write(input_word)
#-----------------------4-masala--------------
# class messenger:
#     def __init__(self,first_name: str, last_name: str,user_name: str,password: str) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.password = password
    
#     def profile(self):
#         print(f"User name: {self.user_name}\nPassword: {self.password}\nFirst name: {self.first_name}\nLast name: {self.last_name}")

#     def passwordd(self):
#         print(f"User name: {self.user_name}\nPassword: {self.password}")

#     def output_message(self):
#         while True:
#             out = input("to Who: ");not_found = 0
#             with open("loginlar.txt") as f:
#                 f.seek(0)
#                 for i in f.read().split("\n"):
#                     if out == i.split(":")[0] and i.split(":")[0] != self.user_name:
#                         self.message(out)
#                         not_found += 1
#                         return 0
#             print(f"User named {out} not found!")
#             print("Do you continue!\n1.Yes 2.No")
#             aaa = int(input(">>> "))
#             if aaa == 2:
#                 break
#     def status(self):
#         friend_lst = []
#         with open(f"{self.user_name}.txt") as f:
#             f.seek(0)
#             for i in f.read().split("\n"):
#                 if i.split(" ")[0] == 'from' and i.split(" ")[1] not in friend_lst:
#                     friend_lst.append(i.split(' ')[1])
#             print('Your friends-->',end=" ")
#             for i in friend_lst:
#                 print(i,end=" ")

#     def message(self,out):
#         with open(f"{out}.txt",'a') as f:
#             f.seek(0);f_count = 0;send_word = f"from {self.user_name}:\n"
#             while True:
#                 send_word += input("Enter you message: ")
#                 send_word += " "
#                 print("Do you send message!\n1.Yes 2.No")
#                 f_a = int(input(">>> "))
#                 if f_a == 2:
#                     break
#             f.write(f"{send_word}\n\n")
#             print("Message send!")
#     def input_message(self):
#         with open(f"{self.user_name}.txt") as f:
#             f.seek(0)
#             for i in f.read().split("\n"):
#                 if i.split(" ")[0] == 'from':
#                     print()
#                     print(f"{i.split(' ')[1]}--> ",end="")
#                 else:
#                     print(i,end="")
# login_count = 0;choise_you = 0
# while True:
#     if choise_you == 0:
#         print("1.Log in         2.Create accaunt      3.End")
#         choise = int(input(">>>> "))
#     if choise == 1:
#         choise_you += 1
#         while True:
#             count = 0
#             user_name = input("enter you username: ")
#             user_pass = input("enter you password: ")
#             with open("loginlar.txt") as f:
#                 f.seek(0)
#                 for i in f.read().split("\n"):
#                     if i.isspace():
#                         break
#                     elif i.split(":")[0] == user_name and i.split(":")[1] == user_pass:
#                         user = messenger(i.split(":")[2],i.split(":")[3],i.split(":")[0],i.split(":")[1])
#                         choise = 2
#                         count += 1
#                         login_count += 1
#                         break
#                     else:
#                         print("user name or password error")
#             if count != 0:
#                 break
#             while True:
#                 print("Do you continue!\n1.Yes 2.No")
#                 b = int(input(">>> "))
#                 if b == 2:
#                     count += 1
#                     choise_you = 0
#                     break
#                 elif b == 1:
#                     count = 0
#                     break
#             if count != 0:
#                 break
#     elif choise == 2:
#         choise_you += 1;enter_count = 0
#         if login_count == 0:
#             name = input("Enter you name: ")
#             surname = input("Enter you last name: ")
#             user_namee = input("Enter you user name: ")
#             passworddd = input("Enter you password: ")
#             user = messenger(name,surname,user_namee,passworddd)
#             with open("loginlar.txt",'a+') as f:
#                 f.seek(0)
#                 for i in f.read().split("\n"):
#                     if i.isspace():
#                         break
#                     if i.split(":")[0] == name:
#                         print("User name is aviable!")
#                         enter_count += 1
#                         choise_you = 0
#                         break
#                 if enter_count == 0:
#                     f.seek(0)
#                     f.write(f"{user_namee}:{passworddd}:{name}:{surname}\n")
#                     with open(f"{user_name}.txt",'w') as f:
#                         pass

#         if choise_you > 0:
#             while True:
#                 print("""
#             1.Profile           2.Status
#             3.Input message     4.Output message
#             5.Password          6.Log out
#             """)
#                 a = int(input(">>>> "))
#                 if a == 1:
#                     user.profile()
#                 elif a == 2:
#                     user.status()
#                 elif a == 4:
#                     user.output_message()
#                 elif a == 3:
#                     user.input_message()
#                 elif a== 5:
#                     user.passwordd()
#                 elif a == 6:
#                     choise_you = 0
#                     login_count = 0
#                     break
#                 else:
#                     print("Not found!")
#     elif choise == 3:
#             print("Thank you!")
#             break
#     else:
#             print("NOt found!")

#-----------------------5-masala-------------
#-----------------------6-masala--------------
#-----------------------7-masala--------------