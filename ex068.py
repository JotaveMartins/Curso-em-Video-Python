import time
from random import randint
cont = 0
x = 'S'
print('=-'*10,'PROGRAMA DA TABUADA','-='*10)
while x != 'N':
    e = str(input('Par ou Impar? [PAR/IMPAR] ')).strip().upper()
    while True:
        mj = randint(1,5)
        pj = int(input('Digite um valor de 1 a 5: '))
        impar = (mj + pj) % 2
        print('~'*20)
        if impar == 0:
            print(f'Você jogou {pj} e a máquina jogou {mj}, somando: {pj+mj} | DEU PAR')
        elif impar == 1:
            print(f'Você jogou {pj} e a máquina jogou {mj}, somando: {pj+mj} | DEU IMPAR')
        print('~'*20)
        if e == 'PAR' and impar == 1 or e == 'IMPAR' and impar == 0:
            break
        elif e == 'IMPAR' and impar == 1 or e == 'PAR' and impar == 0:
            print('\033[42m>>>>O JOGADOR GANHOU ESSA RODADA!\033[m')
            cont +=1
    print('\033[43m>>>>A MÁQUINA GANHOU ESSA RODADA!\033[m')
    print(f'GAME OVER! Você teve {cont} vitórias.')
    x = str(input('Você quer jogar de novo? [S/N] ')).strip().upper()
print('ENCERRANDO PROGRAMA...')
time.sleep(1)
print('PROGRAMA ENCERRADO!')