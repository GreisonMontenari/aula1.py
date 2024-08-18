"""
Estrutura para tratar exceções:
"""

anos = [2019, 2020, 2021]

try:
    ano_atual = anos[3]
    print(ano_atual)
except IndexError:
    print('Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e ' + str(len(anos) - 1))
except Exception as exc:
    print(exc)
    print('Erro genérico')        