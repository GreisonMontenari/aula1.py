"""
Operações
As operações de variáveis do tipo string são:
+ (concatenação)
Concatenação ela junta ou combina, mais de uma string
Para fazer a concatenação é usado o sinal de +
"""

nome = 'Greison Montenari'
sobrenome = 'Ferreira'

apresentacao = 'Olá, meu nome é ' + nome + ' ' + sobrenome + '!'
print(apresentacao)

#### Uma outra forma de concatenar strings é utilizar operações de formatação:

nome = 'Greison Montenari'
sobrenome = 'Ferreira'

apresentacao = f'Olá, meu nome é {nome} {sobrenome}'
print(apresentacao)