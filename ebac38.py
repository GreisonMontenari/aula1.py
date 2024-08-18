"""
if / elif / else
Podemos também avaliar múltipla condições.
"""

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '852'

senha = '7783'
senha_cadastro = '7783'

### Código  Senha  Código And Senha     Mensagem 
### True    True    True                Pagamento efetuado
### True    False   False               Erro: Senha inválida
### False   False   False               Erro: Código de segurança e senha inválidos
### False   True    False               Erro: Código de segurança inválido

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
    print('Pagamento efetuado')

elif (codigo_de_seguranca != codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
    print('Erro: Código de segurança inválido')

elif (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha != senha_cadastro):
    print('Erro: Senha inválida')

else:
    print('Erro: Código de segurança e senha inválidos')    