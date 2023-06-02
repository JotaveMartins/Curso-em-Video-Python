#Exercício de Cálculo de Hipotenusa
from math import hypot
adjascente = float(input('Qual é a medida do cateto adjascente? '))
oposto = float(input('Qual é a medida do cateto oposto? '))
hipotenusa = hypot(oposto, adjascente)
print(f'{hipotenusa:.2f}')