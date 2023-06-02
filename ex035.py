a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
if (a+b>c) and (b+c>a) and (c+a>b):
    print('Essas retas podem formar sim, um triangulo!')
else:
    print('Essas retas não podem formar um triangulo!')