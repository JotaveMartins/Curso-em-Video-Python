ano = int(input('Qual ano você quer checar se é bissexto? '))
if  (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Este ano é Bissexto!')
else:
    print('Este ano não é Bissexto!')
