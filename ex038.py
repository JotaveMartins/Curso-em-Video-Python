n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if  n1 > n2:
    print('O \033[7;30;42mprimeiro\033[m número é maior.')
elif n2 > n1:
    print('O \033[7;30;42msegundo\033[m número é maior.')
elif n1 == n2:
    print('\033[7;30;43mOs números são iguais.\033[m')