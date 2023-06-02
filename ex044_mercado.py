print('\033[7;34m====== 🍇 MERCADINHO DO PROGRAMADOR 👨🏽‍💻 =====\n\033[m')
#====PREÇO DO ALIMENTO====#
arroz = 9.47
feijão = 8.80
queijo = 25.98
ovo = 15
#====PRODUTO COMPRADO====#
print("""\033[1;32mQual produto você deseja comprar?\033[m
[1]Arroz
[2]Feijão
[3]Queijo
[4]Ovo""")
opção = str(input('Selecione: '))
if opção == '1':
    produto = arroz
    a = 'arroz'
    b = arroz
elif opção == '2':
    produto = feijão
    a = 'feijão'
    b = feijão
elif opção == '3':
    produto = queijo
    a = 'queijo'
    b = queijo
elif opção == '4':
    produto = ovo
    a = 'ovo'
    b = ovo
#====FORMA DE PAGAMENTO====#
print("""\033[1;32mEscolha qual será a forma de pagamento:\033[m
[1] PIX/DINHEIRO (Desconto de 10%)
[2] DÉBITO (Desconto de 5%)
[3] CRÉDITO (Sem desconto)""")
opção2 = str(input('Selecione: '))
if opção2 == '1':
    método = produto - (produto * 0.10)
elif opção2 == '2':
    método = produto - (produto * 0.05)
elif opção2 == '3':
    método = (produto)
#====MOSTRANDO====#
print(f'O preço do \033[4;34m{a}\033[m que era \033[4;34mR${b}\033[m, na forma de pagamento escolhida é de: \033[7;32mR${método:.2f}\033[m')
