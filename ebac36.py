"""
Exemplo de if e else
"""
### Exemplo: Código de segurança de um cartão de crédito

codigo_de_seguranca = '837'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

if pode_efetuar_pagamento:
    print('Pagamento efetuado')
else:
    print('Erro: Código de segurança inválido')

if codigo_de_seguranca == codigo_de_seguranca_cadastro:
    print('Pagamento efetuado')
else:
    print('Erro: Código de segurança inválido')    