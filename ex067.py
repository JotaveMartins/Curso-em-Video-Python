import time
cont = n = indice = 0
print('\033[44m',('=-'*10),'PROGRAMA DA TABUADA',('-='*10),'\033[m')
while True:
    cont = indice = 0
    print('-'*40)
    n = int(input('Você quer ver a tabuada de qual número? '))
    print('-'*40)
    if n < 0:
        break
    while cont < 10:
        indice +=1
        cont += 1
        multiplo = n*indice
        print(f'{n} X {indice} = {multiplo}')
print('\033[1;43mENCERRANDO PROGRAMA...\033[m')
time.sleep(1)
print('\033[1;42mPROGRAMA TABUADA ENCERRADO.\033[m')