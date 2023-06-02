numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    escolha = int(input('Digite um número de 0 a 10: '))
    while escolha > 10 or escolha < 0:
        escolha = int(input('Inválido! Tente novamente: '))
    print(f'Você digitou o número {numeros[escolha]}.')
    close = input('Você quer continuar? ').strip().upper()[0]
    if close == 'N':
        print('Programa encerrado!')
        break