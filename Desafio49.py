print('='*20)
tabu = int(input('Digite um numero, te mostro tabuada: '))
print('='*20)
for c in range(1, 11):
    print('{} x {} = {}'.format(tabu, c, tabu*c))
    #print('{} / {} = {}'.format(tabu, c, tabu / c)) >> Outros exemplos de tabuada
    #print('{} + {} = {}'.format(tabu, c, tabu + c))
