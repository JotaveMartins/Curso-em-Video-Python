nome = input('Qual o seu nome? ')
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você irá financiar? '))
meses = anos*12
salario30 = salario*0.30
prestacao = valor/meses
x = meses+60
xa = x/12
if prestacao < salario30:
    print(f'Perfeito! {nome}, o seu financiamento é possível de ser realizado em {anos} anos.')
else:
    if valor/x < salario30:
        print(f"""{nome}, infelizmente com essas condições, não será possível realizar o seu financiamento.
        Para que possamos aprová-lo, ele precisará ser feito em {xa:.0f} anos, e não em {anos}.""")
    else:
        print(f'Senhor(a) {nome},infelizmente, não será possível fazer o seu financiamento nesse momento, até breve!')
