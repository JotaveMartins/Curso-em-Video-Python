print('\033[1;44m=-'*5,'10 Termos de uma PA','-='*5,'\033[m')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} 👉 ',end=(''))
        termo += razão
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer ver? '))
print('FIM!')
print(f'Programa finalizado, foram mostrados {total} termos no total.')