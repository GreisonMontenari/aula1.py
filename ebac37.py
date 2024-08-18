"""
Exemplo: Código e senha de segurança de um cartão de crédito
"""

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '852'

senha = '7783'
senha_cadastro = '7783'

# Revisando a tabela da verdade:

### Código  Senha  Código QR Senha  Código And Senha  Not Código 
### True    True    True             True              False 
### True    False   True             False             False 
### False   False   False            False             True 
### False   True    True             False             True 

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
    print('Pagamento efetuado')
else: 
    print('Erro: Pagamento não efetuado')

if (codigo_de_seguranca != codigo_de_seguranca_cadastro) | (senha != senha_cadastro):
    print('Erro: Pagamento não efetuado')
else:
    print('Pagamento realizado')    
