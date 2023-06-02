tot = 0
for c in range(0,4):
    ano = int(input('Digite o ano de nascimento: '))
    idade = 2023 - ano
    if idade >= 21:
        tot += 1
if tot >1:
    print(f'Das 4 pessoas, {tot} estão na maioridade.')
else:
    print(f'Das 4 pessoas, {tot} está na maioridade')