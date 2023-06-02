#Exercício Conversão de Moedas
valor = float(input('Quanto você tem na conta? '))
print(f'Saldo disponível: R${valor:,.0f}')
dolar = float(5)
euro = float (5.40)
conversaodolar = valor/dolar
conversaoeuro = valor/euro
print(f'Com este valor, é possível fazer a aquisição de:\n {conversaodolar:.2f} dólares.\n {conversaoeuro:.2f} euros.')