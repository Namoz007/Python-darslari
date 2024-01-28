#----------------------------------1---------------
#---------------------------------1-shart--------------------- bajarilmadi

# with open("takrorlash1.txt",encoding="utf-8") as t:
#     year = []
    
#-----------------------------2-shart----------------
# with open("takrorlash1.txt",encoding="utf-8") as t:
#     count = 0
#     for i in t.read().split("\n"):
#         for j in range(4):
#             a = i.split(",")[j]
#             if a[0] == '2':
#                 print(i)
        
#---------------------------------2----------------------qurilma
# with open("takrorlash1.txt") as t:
#     for i in t.read().split("\n"):
#         a = i.split(",")[4]
#         b = a.split(".")[1]
#         if int(b) > 5 and int(b) < 9:
#             print(i)
#--------------------------------3------------------------ishga kirgan
#------------------------------1-shart--------------------
# with open('takrorlash1.txt') as t:
#     for i in t.read().split("\n"):
#         year = i.split(",")[3]
#         year1 = year.split("-")[2]
#         hisob = 2023 - int(year1)
#         if hisob > 18:
#             print(i)
#------------------------------2-shart-----------
# with open("takrorlash1.txt") as t:
#     for i in t.read().split("\n"):
#         year = i.split(",")[4]
#         year1 = year.split("-")[2]
#         hisob = 2023 - int(year1)
#         if hisob > 20:
#             print(i)
#------------------------------4-----------------xato malumot
#-----------------------------1-shart-------------
# with open("takrorlash1.txt") as t:
#     for i in t.read().split("\n"):
#         if i.split(",")[3] == 'false':
#             print(i)
#-----------------------------2-shart--------------
# with open("takrorlash1.txt") as t:
#     for i in t.read().split("\n"):
#         year = i.split(",")[2]
#         if  2023 - int(year.split("-")[2]) > 20:
#             print(i)
#-----------------------------3-shart---------------
# with open("takrorlash1.txt") as t:
#     st = set()
#     for i in t.read().split("\n"):
#         st.add(i.split(",")[0])
#     for i in st:
#         print(i)
# ----------------------------------------------------