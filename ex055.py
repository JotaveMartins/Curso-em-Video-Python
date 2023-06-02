tot = 0
for c in range(0,5):
    peso = int(input('Digite um peso: '))
    if tot < peso:
        tot = peso
print(tot)