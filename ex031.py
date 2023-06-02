d = int(input('Qual a distancia você percorreu em km? '))
p1 = 0.50
p2 = 0.45
if  d>200:
    pf = d*p2
else:
    pf = d*p1
print(f'O valor total da sua viagem baseado nos {d}km percorridos é de: R${pf:.2f}')