palavras = ('AMARELO','PRETO','BRANCO','AZUL')
for p in palavras:
    print(f'\nEm {p} temos: ',end='')
    for v in p:
        if v in 'AEIOU':
            print(f'{v}',end=' ')