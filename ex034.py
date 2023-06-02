s = int(input('Qual o seu salário? '))
a1 = s*1.10
a2 = s*1.15
if s>1250:
    print(f'O novo salário agora será de R${a1:,.2f}!')
if s<=1250:
    print(f'O novo salário agora será de R${a2:,.2f}!')
print('Parabéns pelo seu aumento!')