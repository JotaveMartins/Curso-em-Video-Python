#Exercício Cálculo de área
largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))
area = largura*altura
tinta = (2**2)
resultadotinta = (area/tinta)
print(f'A área desta parede é: {area:.0f} metros quadrados.')
print(f'E a quantidade de litros de tinta para pintá-la é: {resultadotinta:.0f} litros')