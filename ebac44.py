"""
Estrutura para tratar exceções:
"""

anos = [2019, 2020, 2021]

try:
    ano_atual = anos[3]
    print(ano_atual)
except Exception: ### Exception vai pegar qualquer tipo de exceção (caso voce nao saiba a exceção)
    print('Lista de anos é menor que a valor escolhido. Espera-se um valor entre 0 e ' +str(len(anos) -1))    