#A solução abaixo fiz antes da resposta, deu certo, mas não era o resultado que o exercio pedia.
##for c in range (1, 6):
#    peso = float(input('Qual seu peso? '.format(c)))
#    if peso >= 70:
#       print('Vocês tá acima do peso!')
#    else:
#        print('Você está no peso ideal! Parabéns!')

print('='*25)
print('→ Coloque seu peso abaixo:')
print('='*25)

maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('→ O maior peso verificado foi de {}Kg'.format(maior))
print('→ O menor peso verificado foi de {}Kg'.format(menor))