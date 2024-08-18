"""
Operações de diferença
Ela tira a diferença dos conjuntos.
As operações da estrutura do tipo set são.
-(diferença)
"""

norte_europa = {'reino unido', 'suecia', 'russia', 'noruega','dinamarca'}
escandinavia = {'noruega', 'dinamarca', 'suecia'}

norte_europa_nao_escandivano = norte_europa - escandinavia
print(norte_europa_nao_escandivano)

escandivano_nao_norte_europa = escandinavia - norte_europa
print(escandivano_nao_norte_europa)