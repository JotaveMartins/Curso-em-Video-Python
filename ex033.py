n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#===========MENOR
menor = n1
if  n2<n1:
    menor = n2
if n3<menor:
    menor = n3
#===========
#===========MAIOR
maior = n1
if n2>maior:
    maior = n2
if n3>maior:
    maior = n3
#===========
#===========RESULTADO:
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')