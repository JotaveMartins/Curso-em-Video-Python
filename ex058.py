from random import randrange
n = randrange(1,11)
print(n)
print('\033[7;34m=-'*10,'ADVINHE O NÚMERO','-='*10,'\033[m')
tentativas = 1
np = int(input('Qual número entre 1 a 10 você acha que o computador jogou?\n '))
while np != n:
    print('Você errou!')
    np = int(input('Tente novamente: '))
    tentativas += 1
else:
    print(f'Você acertou depois de {tentativas} tentativas!')
