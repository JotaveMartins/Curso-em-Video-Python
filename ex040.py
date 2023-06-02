print('='*10,'\033[7;32;40mREPROVOU OU NÃO?\033[m','='*10)
n1 = float(input('Digite a nota de Matemática: '))
n2 = float(input('Digite a nota de Geografia: '))
média = (n1+n2)/2
if média > 7.0:
    print('Meus parabéns!! Você está \033[4;32mAPROVADO(A)\033[m!')
elif média < 5.0:
    print('Infelizmente, \033[4;31mo aluno foi reprovado\033[m direto!')
else:
    print('Ainda não está perdido! Você tem uma nova chance na \033[4;33mrecuperação\033[m.')
