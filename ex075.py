print('-----EXERCÍCIO_TUPLAS-----')
tupla = int(input('Digite um número: ')),int(input('Digite um outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: '))
print('-'*40)
print(f'Os números escolhidos foram: {tupla}.')
print('-'*40)
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
print('-'*40)
if 3 not in tupla:
    print(f'Nenhum número 3 foi digitado.')
else:
    print(f'O número 3 apareceu a primeira vez na posição {tupla.index(3) + 1}.')
print('-'*40)
print(f'Os números pares são: ',end='')
for n in (tupla):
    if n % 2 == 0:
        print(n,end=' ')
