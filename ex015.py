#Exercício de Aluguel de Carro
#====REGRA====#
pkm = float(0.15)
pdia = int(60)
#====DEFINIÇÕES====#
km = int(input('Quantos kilômetros foram percorridos com o carro? '))
dias = int(input('Quantos dias você ficou com o carro? '))
#====CÁLCULO====#
rkm = (pkm*km)
rdia = (pdia*dias)
rtotal = (rdia+rkm)
#====RESPOSTA====#
print(f'O total a pagar é de: R${rtotal:,.2f}')