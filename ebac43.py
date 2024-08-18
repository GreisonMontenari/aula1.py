"""
Estrutura para tratar exceções:
"""

preco = 132.85
pessoas = 0

try: 
    valor_por_pessoa = preco / pessoas
    print(valor_por_pessoa)
except ZeroDivisionError:
    print('Número de pssooas inválido. Espera-se um valor maior que 0 e obteve-se um valor igual a ' + str(pessoas))    