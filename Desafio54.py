from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 4): #aparecem 3 pessoas. Se quero 5 pessoas, coloco número 6, sempre um número a mais do que quero.
    num = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - num
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print ('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))




