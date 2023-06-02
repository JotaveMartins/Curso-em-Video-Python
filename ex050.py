s = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    par = n % 2
    if par == 0:
        s += n
print(f'O resultado foi {s}')