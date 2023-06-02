ci = cm = cf = 0
while True:
    print('-'*25)
    print(''*5,'CADASTRE UMA PESSOA',''*5)
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('-'*25)
    if idade > 18:
         ci +=1
    if sexo == 'M':
         cm += 1
    if sexo == 'F' and idade < 20:
        cf += 1
    f = str(input('Você quer continuar? ')).strip().upper()[0]     
    if f == 'N':
        print('=-'*20)
        break
print(f'''Número de pessoas acima de 18 anos: {ci}\n
Número de Homens cadastrados: {cm}\n
Número de Mulheres que tem menos de 20 anos: {cf}\n''')