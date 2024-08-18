"""
Exemplo de booleano(bool)
Sempre use o bool como se fosse uma pergunta
"""
### Caixa eletrônico

saldo_em_conta = 300
valor_do_saque = 100
pode_executar_saque = valor_do_saque <= saldo_em_conta  ### Exemplo de usar como pergunta
print(pode_executar_saque)

### Exemplo: Cartão de crédito

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro ### Exemplo de usar como pergunta
print(pode_efetuar_pagamento)