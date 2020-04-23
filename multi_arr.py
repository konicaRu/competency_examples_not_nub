import copy
lst = []
c=[]
while True:
    a = input()
    if a == 'end':
        break
    lst += [a.split()]
for i in range(len(lst)):
 b = [int (j) for j in lst[i]]
 c.append(b)
b = copy.deepcopy(c)
for i in range(len(c)):
    for j in range(len(c[i])):
        f = len(c[0])
        e= len(c)
        d = (c[i][(j - 1) % f] + c[i][(j + 1) % f] + c[(i + 1) % e][j] + c[(i - 1) % e][j])
        b[i][j] = d
for i in range(len(b)):
    print()
    for j in range(len(b[i])):
     print(b[i][j], end=' ')