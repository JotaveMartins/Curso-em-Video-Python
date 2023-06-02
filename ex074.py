from random import randint
menor = 11
maior = 0
print('Os valores sorteados foram: ',end='',)
for x in range(0,5):
    c = randint(0,10)
    print(f'{c}',end=' ')
print('\n','-'*30)
print(f'O maior valor foi: {max(maior)}')
print('-'*30)
print(f'O menor valor foi: {min(menor)})')
print('-'*30)