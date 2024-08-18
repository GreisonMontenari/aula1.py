"""
Dicionário ele é composto por uma por um valor. 
Esse valor pode ser arbritario 
For / in / dict
Estrutura que permite a execução de um bloco
de código para todos os elementos de um dicioário.
"""
### credito conte 3 senhas de 3 pessoas e o escore dessas pessoas

credito = {'123': 750, '456': 812, '789': 980}

for valor in credito.values():
            print(valor)
            print(f'O valor do escore de crédito é {valor}, mas não temos mais chaves:(.)')
            print('\n') ### pular linha, assim o código fica mais limpo