#Exercício de Sorteio de Ordem
from random import choice, choices, shuffle
t1 = input('Qual o primeiro time? ')
t2 = input('Qual o segundo time? ')
t3 = input('Qual o terceiro time? ')
t4 = input('Qual o quarto time? ')
lista = [t1, t2, t3, t4]
shuffle(lista)
print(f'A ordem da apresentação será:\n{lista}')
