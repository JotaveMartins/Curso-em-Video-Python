v = float(input('Qual a velocidade do carro? '))
multa = v*7
if  v >80:
    print(f'Você ultrapassou o limite de velocidade, recebeu uma multa no valor de R${multa:.2f}!')
else:
    print('Tudo certo, você passou dentro do limite de velocidade!')