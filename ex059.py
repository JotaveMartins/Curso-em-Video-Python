import time
print('\033[1;46m=-'*6,'PROGRAMA INICIADO','-='*6,'\033[m')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
r = 0
maior = 0
print(f'Os números são: {n1} e {n2}.')
f = "Não"
while f != "Sim":
    m = n1*n2
    s = n1+n2
    time.sleep(1.5)
    print("""Opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Fechar o programa""")
    r = int(input(">>>>> Sua escolha: "))
    if r < 1 or r > 5:
        print('\033[1;31mOpção inválida!\033[m Tente novamente.')
    else:
        if r == 1:
            print(f"A resposta é {s}!")
        elif r == 2:
            print(f"A resposta é {m}!")
        elif r == 3:
            if n1 < n2:
                maior = n2
            else:
                maior = n1
            print(f"O maior número é: {maior}")
        elif r == 4:
            print("Agora você pode digitar o novos números")
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            print(f'Os novos números são: {n1} e {n2}')
        print('=-'*15)
        if r == 5:
            print('Encerrando programa...')
            time.sleep(1)
            f = 'Sim'
print("\033[1;34;42mPrograma encerrado! Siga o @dozeroaprogramacao!\033[m")
