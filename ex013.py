#Exercício Cálculo de Aumento no Salário
funcionario = input('Qual o nome do funcionário? ')
salario = float(input(f'Qual o salário do {funcionario}? '))
qualporcentagem = int(input('Qual o aumento em % você dará ao funcionário? '))
porcentagem = (qualporcentagem/100)
salarioaumento = salario+(salario*porcentagem)
print(f'O novo salário de {funcionario} será: R${salarioaumento:,.0f}.')
