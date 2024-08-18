"""
Motivação
Dicionários: Para você se conectar a uma rede wi-fi, você precisa de duas
infoarmações: o nome da rede e a senha de acesso. Quando você vai acessar
uma nova rede, você encontra uma lista de redes disponíveis:
"""

wifi_disponiveis = ['rede1', 'cnx_cnx', 'uai-fi', 'r3d3']
print(wifi_disponiveis)

### Você consegue identificar quais são os nome de redes e suas 
### respectivas senhas? Talvez uma list não seja a melhor opção para 
### armazenar esse tipo de dado.

wifi_disponiveis = []

rede = {'nome': 'rede1', 'senha': 'cnx_cnx'}
wifi_disponiveis.append(rede)

rede = {'nome': 'uai-fi', 'senha': 'r3d3'}
wifi_disponiveis.append(rede)

print(wifi_disponiveis)