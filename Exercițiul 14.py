n = int(input('Dați numărul de linii: '))
m = []
for i in range(0, n):
    a = []
    for j in range(0, n):
        a.append(int(input('> ')))
    m.append(a)
for i in range(0, n):
    for j in range(0, n):
        print(m[i][j], end = " ")
    print()
sumdp = 0
for i in range(0, n):
    sumdp += m[i][i]
print('Suma elementelor de pe diagonala principală: ', sumdp)
sumds = 0
c = 0
for i in m[::-1]:
    sumds += i[c]
    c += 1
print('Suma elementelor de pe diagonala secundară: ', sumds)
sumdps = 0
sumdpj = 0
for i in range(0, n):
    for j in range(0, n):
        if i < j:
            sumdps += m[i][j]
        if i > j:
            sumdpj += m[i][j]
print('Suma elementelor aflate mai sus de diagonala principală: ', sumdps)
print('Suma elementelor aflate mai jos de diagonala principală: ', sumdpj)
sumdss = 0
sumdsj = 0
for i in range(0, n):
    for j in range(0, n):
        if (i + j) < (n - 1):
            sumdss += m[i][j]
        if (i + j) > (n - 1):
            sumdsj += m[i][j]
print('Suma elementelor aflate mai sus de diagonala secundară: ', sumdss)
print('Suma elementelor aflate mai jos de diagonala secundară: ', sumdsj)