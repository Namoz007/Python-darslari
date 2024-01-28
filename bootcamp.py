# lst = []
# for i in range(int(input("Nechta qiymat kiritmoqchisiz: "))):
#     dct = {
#         'name' : input("Mahsulot nomi: "),
#         'price' : int(input("Narxi qancha: "))
#     }
#     lst.append(dct)
# count = 0;serach = ''
# for i in lst:
#     pricee = 0
#     for j in dict(i).values():
#         if isinstance(j,int):
#             if int(j) > count:
#                 count = int(j)
#                 serach = i
# print(serach)



# a = input('Son kiriting: ')
# count = 0
# for i in a:
#     if i == '0':
#         count += 1
#     elif i != '0':
#         break
# print(count)



with open('bootcamp_input.txt') as f:
    word = f.read()
new_word = '';lst = []
for i in word:
    new_word += i
    lst.append(new_word)
new_lst = []
for i in lst:
    new_lst.append(i)
new_lst.reverse()
new_lst.remove(word)
for i in new_lst:
    lst.append(i)
print(lst)