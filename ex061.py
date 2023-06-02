print('\033[1;44m=-'*5,'10 Termos de uma PA','-='*5,'\033[m')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} 👉 ',end=(''))
    termo += razão
    cont +=1
print('Fim!')