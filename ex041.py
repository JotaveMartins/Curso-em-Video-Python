nascimento = int(input('Digite qual o ano em que você nasceu: '))
idade = 2023 - nascimento
if idade <= 9:
    print('Mirim')
elif idade >9 and idade <=14:
    print('Infantil')
elif idade >14 and idade <=19:
    print('Junior')
elif idade == 20:
    print('Sênior')
elif idade >20:
    print('Master')