times = ('Flamengo','Santos','Palmeiras','Grêmio','Atlético Paranaense','São Paulo','Internacional','Corinthians','Fortaleza','Goiás')
print('-'*35)
print('Os \033[4;32mTop 5\033[m do campeonato são:')
print('-'*35)
for cincoPrimeiros in times[0:5]:
    print(f'>>> {cincoPrimeiros}')
print('-'*25)
print('Os \033[4;31multimos quatro\033[m são:')
print('-'*25)
for quatroUltimos in times[-4:10]:
    print(f'>>> {quatroUltimos}')
print('-'*35)
print('Em ordem \033[4;33malfabética\033[m os times ficam:')
print('-'*35)
x = sorted(times)
for alfa in x[0:10]:
    palmeiras = sorted(times)[7]
    santos = sorted(times)[8]
    sp = sorted(times)[9]
    if alfa != santos and alfa != sp:
        if alfa != palmeiras or alfa == palmeiras:
            print(f'{alfa}',end=', ')
    if alfa == sp:
        print(f'{alfa}.')
        break
    if alfa == santos:
        print(f'{alfa} e ',end='')
print('-'*45)
time = str(input('Qual time você quer olhar a posição? '))
cont = 0
for c in times:
    if c != time:
        cont += 1
    if c == time:
        break
print('-'*45)
print(f'>>> O {time} está em {cont + 1}º no ranking!')
print('-'*30)
print('\033[42m-----PROGRAMA ENCERRADO-----\033[m')
print('-'*30)