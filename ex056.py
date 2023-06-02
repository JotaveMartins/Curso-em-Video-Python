toti = 0
totih = 0
totm = 0

for c in range(0,4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    toti += idade
    sexo = input('Sexo: ')
    if totih < idade and sexo == 'Masculino':
        totih = idade
        hv = nome
    if sexo == 'Feminino' and idade < 20:
        totm += 1
    print('=-'*10)

média = toti / 4
print(f'A média de idade do grupo é: {média:.0f}')
print(f'O homem mais velho do grupo é o {hv}')
print(f'E a quantidade de mulheres que tem menos de 20 anos é {totm}.')