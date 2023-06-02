sexo = str(input('Informe o seu sexo (M/F): ')).strip().upper()[0]
n1 = 'Masculino'
n2 = 'Feminino'
while sexo not in 'MF':
    print('Resposta inválida')
    sexo = (input('Tente novamente: ')).strip().upper()[0]
if sexo == 'M':
    print(f'O sexo escolhido foi {n1}.')
if sexo == 'F':
    print(f'O sexo escolhido foi {n2}.')