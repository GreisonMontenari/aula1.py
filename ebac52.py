"""
For / in / list
Estrutura que permite a execução de um bloco
de código para todos os elementos de uma lista.
"""

frase = 'Fala pessoal, meu nome é Greison Montenari.'

for caracter in frase:
    if (caracter == 'G') | (caracter == 'z'):
        print(f'A letra "{caracter}" está presente na frase.')
       