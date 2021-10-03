n = int(input('Câte cifre vreți să introduceți? '))
numere = []
for i in range(0, n):
    num = int(input('> '))
    numere.append(num)
cod = str(input('În ce cod doriți ca numerele să fie afișate? (ASCII, Gray, Aiken, Exces 3) '))
codl = [['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001'],
    [ '0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100', '1100', '1101'],
    [ '0000', '0001', '0010', '0011', '0100', '1011', '1100', '1101', '1110', '1111'],
    [ '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100']]
if (cod == 'ASCII'):
    rand = codl[0]
elif (cod == 'Gray'):
    rand = codl[1]
elif (cod == 'Aiken'):
    rand = codl[2]
elif (cod == 'Exces 3'):
    rand = codl[3]
s = ''
for j in range(0, len(numere)):
    s += rand[int(numere[j])] + ' '
print(s)