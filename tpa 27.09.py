m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print('a)') 
for i in m:
    print('Suma rândului', m.index(i)+1, '=', sum(i))
sumr = 0
print('b) ')
for j in range(0, 3):
    for k in m:
        sumr += k[j]
    print('Suma coloanei', j+1, '=', sumr)
dp = []
for l in range(0, 3):
    dp.append(m[l][l])
print('c) ')
print('Diagonala principală:', *dp)
ds = []
c = 2
for b in range(0, 3):     
    ds.append(m[b][c])
    c -= 1
print('d) ')
print('Diagonala secundară: ', *ds)