n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    d = n % c
    if d == 0:
        print(f'\033[33m',end='')
        tot += 1
    else:
        print('\033[31m',end='')
    print(f'{c} ',end='')
print(f'\033[m\nO número {n} foi dividido {tot} vezes.')
if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')