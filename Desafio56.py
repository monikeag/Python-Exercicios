somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('----- {}º pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo  [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn': #in é caso o usuário digite minuscula ou maiuscula, o sistema reconhecer.
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
mediaidade = somaidade / 4
print ('A média de idade do grupo é de {} anos'.format(mediaidade))
print ('O homen mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print ('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))