pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pri + (100-1) * raz #so pq quero o decimo termo. para outro valor, mudar para outro 4
for c in range (pri, dec + raz, raz):
    print('{}'.format (c), end='→ ')
print ('\033[1;33m Acabou\033[m')