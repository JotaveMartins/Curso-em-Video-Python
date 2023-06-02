#Exercício Tabuada do número
numero = int(input("Digite o número para qual você quer ver a tabuada: "))

for indice in range(1, 11):
    tabuada = numero * indice
    print(f'{numero} x {indice} = {tabuada}')
