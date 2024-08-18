"""
Estrutura para tratar exceções:
try / except / finally
Finally ela vai adicionar um elemento nessa estrutura que 
sempre vai ser executado. Nao importa se o código apresentou
erro
"""

nome = 'Greison Montenari'
idade = 36

try: 
    apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos '
    print(apresentacao)
except TypeError: 
    idade = str(idade)
finally:
    print('Segunda chance')
    apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos '
    print(apresentacao)        