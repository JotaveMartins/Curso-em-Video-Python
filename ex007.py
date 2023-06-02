#Exercício Média
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = ((nota1+nota2)/2)
print(f'A média de notas da aluna {nome} é: {media}')
if media >=float('7'):
    print(f'Parabéns {nome}! Você está na média.')
else: print('Menina feia, estude mais.')