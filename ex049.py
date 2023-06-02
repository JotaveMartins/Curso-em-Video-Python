loop = 'Sim'
while loop == 'Sim':
    n = int(input('Digite o número que você quer consultar a tabuada: '))
    for indice in range(1,11):
        tabuada = n * indice
        print(f'{n} x {indice} = {tabuada}')
    loop = input('Você quer consultar novamente? ')
if loop == 'Não':
    print('Até mais')