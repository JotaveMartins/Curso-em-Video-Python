#Exercício de Conversão de Temperaturas

tipo = input('Você quer colocar a temperatura em qual medida? ')
if tipo =='Celsius':
    temperaturacelsius = float(input('Qual a temperatura atual em celsius? '))
    fahrenheit = (temperaturacelsius * 1.8) + 32
    if tipo =='Celsius':
        print(f'{temperaturacelsius:.1f}ºC convertido em graus fahrenheit é igual a: {fahrenheit:.1f}ºF')

if tipo =='Fahrenheit':
    temperaturafahrenheit = float(input('Qual a temperatura atual em fahrenheit? '))
    celsius = (temperaturafahrenheit - 32) / 1.8
    if tipo =='Fahrenheit':
        print(f'{temperaturafahrenheit:.1f}ºF convertido em graus celsius é igual a: {celsius:.1f}ºC.')



