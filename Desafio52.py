#Programa que leia um número inteiro e diga se é ou não número primo.
num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[34m', end=(' '))
        tot += 1
    else:
        print('\033[37m', end=(' '))
    print('{}'.format(c), end=(' '))
print ('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
   print ('E por isso é um número PRIMO')
else:
    print ('E por isso NÃO é número primo')


