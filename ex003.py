x = int(input('Qual o primeiro número? '))
y = int(input('Qual o segundo número? '))
print('O resultado da soma é', y + x)
print('E multiplicando, o resultado é', x * y)
resposta = (input('Está correto? '))
if resposta == 'Sim':
    print('Muito bom!')
else:
    print('Que pena.')
