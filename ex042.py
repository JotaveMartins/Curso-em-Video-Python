r1 = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida da terceira reta: '))
if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print('Essas retas podem sim, formar um triângulo!')
else:
    print('Não, essas retas não podem formar um triângulo!')
if r1 == r2 == r3:
    print('E ele é um triângulo: Equilátero')
elif r1 != r2 != r3:
    print('E ele é um triângulo: Escaleno')
elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
    print('E ele é um triângulo: Isósceles')


