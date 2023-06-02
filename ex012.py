#Exercício Cálculo de Desconto
#==========PRODUTOS====================
arroz = float(10.03)
feijão = float(8.27)
carne = float(20.30)
frango = float(12.50)
#==========CONDIÇÃO====================
loop = 'Sim'
#==========SE FOR ARROZ====================
while loop == 'Sim':
    produto = input('Qual o produto você vai aplicar o desconto? ')
    if produto =='arroz' :
        arrozdesconto = (arroz-(arroz*0.05))
        print(f'Preço final do arroz com 5% de desconto: R${arrozdesconto:.2f}')
    #==========SE FOR FEIJÃO====================
    if produto =='feijão' :
        feijaodesconto = (feijão-(feijão*0.05))
        print(f'Preço final do feijão com 5% de desconto: R${feijaodesconto:.2f}')
    #==========SE FOR CARNE====================
    if produto =='carne' :
        carnedesconto = (carne-(carne*0.05))
        print(f'Preço final da carne com %5 de desconto: R${carnedesconto:.2f}')
    #==========SE FOR FRANGO====================
    if produto =='frango' :
        frangodesconto = (frango-(frango*0.05))
        print(f'Preço final do frango com 5% de desconto: R${frangodesconto:.2f}')
    loop = input('Deseja adicionar mais um produto ao desconto? ')
