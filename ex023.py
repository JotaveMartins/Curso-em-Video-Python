#Exercício de Nome
cidade = (input('Digite o nome de uma cidade: '))
resposta = str('Santo' in cidade)
if resposta == 'True':
    print('No nome dessa cidade tem (Santo).')
else:
    print('No nome não tem (Santo).')