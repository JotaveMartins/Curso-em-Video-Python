#Exercício de Nome
#=====NOME=====#
nome = input('Qual o seu nome? ')
nomesemespaco = nome.lstrip().rstrip().split()
nomeup = nome.upper()
nomelow = nome.lower()
#=====PRIMEIRO NOME=====#
primeironome = nomesemespaco[0]
primeironomefinal = len(primeironome)
#=====NOME COMPLETO=====#
nomecompleto = nomesemespaco
nomejunto = ''.join(nomecompleto)
completofinal = len(nomejunto)
print('='*20)
print(f'O nome apenas em carácteres maiúsculos é: {nomeup}')
print(f'O nome apenas em carácteres minúsculos é: {nomelow}')
print(f'O nome completo tem no total: {completofinal} carácteres')
print(f'O primeiro nome tem no total: {primeironomefinal} carácteres')