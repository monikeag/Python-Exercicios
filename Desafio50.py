soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:  # % quer dizer for ( se o num for 2...)
        soma += num  # ou soma = soma + num
        cont += 1    # ou cont + 1  - A forma como coloquei é a simplificada.
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
