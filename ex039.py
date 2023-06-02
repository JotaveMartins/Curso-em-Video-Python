print('='*10,'\033[1;30;42mALISTAMENTO MILITAR\033[m','='*10)
nome = input('Digite qual o seu nome: ')
nascimento = int(input('Digite em qual ano você nasceu: '))
idade = 2023 - nascimento
diferença = idade - 18
if idade == 18:
    print(f'{nome} \033[4;30;42mestá na hora\033[m de você se apresentar na junta militar mais próxima!')
elif idade > 18:
    print(f'{nome} você já se apresentou na junta militar há \033[4;30;42m{diferença} ano(s)\033[m.')
elif idade < 18:
    x = str(diferença)
    print(f'{nome} faltam \033[4;30;42m{x[1:]} ano(s)\033[m para você se apresentar na junta militar.')

