"""
Conversão
Podemos converter as chaves e os items de um 
dicionário em uma lista.
"""

artigo= dict(
    titulo='Módulo 02 | Python: Estruturas de Dados',
    corpo='Tópics, Aulas, Listas, Conjuntos, Dicionários, ...',
    total_caracteres=1350
)

chaves = list(artigo.keys())

print(chaves)
print(type(chaves))

valores = list(artigo.values())

print(valores)
print(type(valores))