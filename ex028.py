import random
n1 = str(random.randrange(1,5))
loop = 'Sim'
while loop =='Sim':
    resposta = str(input('De 0 a 5, qual número você acha que o computador escolheu? '))
    if resposta ==n1:
        input('Parabéns!! Você acertou')
    else:
        loop = input('Errou, você quer tentar de novo? ')