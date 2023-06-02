valor = int(input('Valor para saque: '))
total = valor
ced = 50
contCed = 0
while True:
    if total >= ced:
        total -= ced
        contCed += 1
    else:
        if contCed > 0:
            print(f'Total de {contCed} de R${ced}.')
        if ced == 50:
            contCed = 0
            ced = 20
        elif ced == 20:
            contCed = 0
            ced = 10
        elif ced == 10:
            contCed = 0
            ced = 1
        if total == 0:
            break