lista = ('Caderno',12.5,'Lápis',2.0,'Cola',5.0,'Borracha',1.0,'Estojo',15.0)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R$ {lista[pos]:.2f}')
print('-'*40)