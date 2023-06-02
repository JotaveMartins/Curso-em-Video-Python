fechar = 0
soma = 0
while fechar != 999:
    fechar = int(input('Digite um número: '))
    soma += fechar
resultado = soma - 999
print(f'A soma de todos os números até o final é de {resultado}')
