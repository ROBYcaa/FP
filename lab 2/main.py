# def p1(list):
#
#     for x in list:
#         if list.count(x) > 1:
#             list.remove(x)
#     return list
#
# list = [85, 75, 75 , 65]
# res = p1(list)
# print(res)
#
# /
l1 = [31, 13, 50, 13]

def p2(l1):
    contor = 0
    for i in range(0,len(l1)):
        for j in range(i+1,len(l1)):
            if int(l1[i] % 10) == int(l1[j] // 10) and int(l1[i] // 10) == int(l1[j] % 10):
                contor += 1
    return contor
m = p2(l1)
print(m)



def p3(l1):
    nr = []
    while len(l1) != 0:
        max_loc = 0
        for i in range(len(l1)):
            if l1[i] > max_loc:
                max_loc = l1[i]
                icop = i #
        nr = str(nr) + str(max_loc)
        del l1[icop] #
    return nr[2:]
l1 = [31, 13, 50]
print(p3(l1))


def p3(metoda,l):
    res = []
    if metoda == '+':
        for el in l:
            res.append(el + l[0])
    if metoda == '*':
        for el in l:
            res.append(el * l[0])
    return res

l = [7, 2, 3, 4] #apelam functia
k = p3('*', l)

print(k)

