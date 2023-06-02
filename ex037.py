n = int(input('Digite um número: '))
print("""Escolha uma das bases de conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL""")
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'O número {n} convertido em \033[4;;mbinário\033[m é {bin(n)[2:]}')
elif opção == 2:
    print(f'O número {n} convertido em \033[4;;moctal\033[m é {oct(n)[2:]}')
elif opção == 3:
    print(f'O número {n} convertido em \033[4;;mhexadecimal\033[m é {hex(n)[2:]}')
else:
    print('Resposta Inválida! Tente novamente.')