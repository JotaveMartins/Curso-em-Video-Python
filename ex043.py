peso = float(input('Diga ao programa qual o seu peso: '))
altura = float(input('Diga ao programa qual a sua altura: '))
imc = peso // (altura*altura)
if imc < 18.5:
    print('\033[1;33mAbaixo do peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[1;32mPeso ideal\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1;33mSobrepeso\033[m')
elif imc > 30 and imc < 40:
    print('\033[1;31mObesidade\033[m')
elif imc > 40:
    print('\033[4;31mObesidade Mórbida\033[m')
x = str(imc)
print(x[:4])
