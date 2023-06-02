f = 'Não'
nm = 0
soma = 0
menor = 100
maior = 0
while f != 'N':
    n = int(input('Digite um número: '))
    nm += 1
    soma += n
    if n > menor:
        menor = menor
    if n < menor:
        menor = n
    if n < maior:
        maior = maior
    if n > maior:
        maior = n
    f = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
média = soma/nm
print(f'A média entre todos os números digitados é de {média:.1f}, o maior número digitado foi {maior} e o menor foi {menor}.')