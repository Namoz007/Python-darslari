#masala 

#1

# tpl = (1,2,3,5,9,6,1)
# count = 0
# for i in tpl:
#     count += i
# print(count)


#2

# tpl = (1,2,3,5,9,6,1)
# max = tpl[0]
# min =  tpl[0]
# for i in tpl:
#     if i > max:
#         max = i
    
#     if i < min:
#         min = i
# print(max - min)


#3     

# tpl = (1,2,3,5,9,6,1)
# a = list(tpl)
# a.remove(max(a))
# tpl = tuple(a)
# print(tpl)


#4

# tpl = ("salom",'kim','kim','nima','yanachi','nsdfjalslk')
# tpl2 = []
# for i in tpl:
#     if len(i) > 5:
#         tpl2.append(i)
# print(tpl2)


#5

# tpl = [(1,2),(5,6,1),(1,9),(5,4)]

# count = 0
# for i,v in enumerate(tpl):
#     tpl[i] = sum(v)
# print(tpl)


#6
# tpl = [(1,2,3),(2,2),(3,0,0)]
# tpl.sort(key=lambda x: sum(x))

# print(tpl)\



#7

# tpl = [(1,2),(3,4),(8,9)]
# tpl1 = []
# tpl2 = []
# tpll = []
# for i in tpl:
#     tpl1.append(i[0])
#     tpl2.append(i[1])

# tpll.append(tuple(tpl1))
# tpll.append(tuple(tpl2))
# print(tpll)

#8

# tpl = [[1,2,3],[4,5,6],[9,27],[2,0,10],[0,1],[1],[2,2,2]]
# print(max(tpl))  

#9

# tpl = [(0,1,0,0),(5,4,3,4),(2,2,6,2)]
# tpl1 = list(tpl)

# for i,v in enumerate(tpl1):
#     for j,k in enumerate(tpl1):
#         n = tpl1[i].count(k)
#         tpl1[i][j] = n
# print(tpl1)


#keyingi masala

#1
import subprocess

nw = subprocess.check_output(['netsh','wlan','show','network'])
decoded_nw = nw.decode('ascii')
print(decoded_nw)