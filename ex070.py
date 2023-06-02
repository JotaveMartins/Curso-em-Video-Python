produto_mais_barato = 1000000000
nome_mais_barato = 'x'
maior_que_mil = total = 0
while True:
    print('-'*20)
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    while preco < 0:
        preco = float(input('Preço: '))
    total += preco
    if preco > 1000:
        maior_que_mil +=1
    if produto_mais_barato > preco:
        produto_mais_barato = preco
        nome_mais_barato = produto
    fechar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while fechar not in 'SN':
        fechar = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if fechar == 'N':
        print('-'*15)
        break
print(f'''O total gasto na compra é de R${total:.2f}.\n
{maior_que_mil} produtos custaram acima de R$1000.\n
O produto mais barato foi o: {nome_mais_barato} que custa {produto_mais_barato:.0f}''')