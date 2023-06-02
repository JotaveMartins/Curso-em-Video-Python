numero = int(input('Qual o número você quer ver se é impar ou par? '))
resto = numero % 2
if  resto ==0:
    print('Este número é par!')
else:
    print('Este número não é par!')