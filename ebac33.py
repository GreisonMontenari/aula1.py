"""
Métodos
São métodos nativos do Python que nos ajudam a trabalhar no dia a dia
com dicionários.
"""

artigo = dict(
     titulo='Modulo 02 | Python: Estrutura de Dados',
     corpo='Topicos, Aulas, Listas, Conjuntos, Dicionários, ...',
     total_caracteres=1530
)

### adicionar/atualizar um elemento pelo chave-valor: dict.update(dict)
print(artigo)
artigo.update({'total_caracteres: 7850'})
print(artigo)

### remover um elemento pelo chave: dict.pop(key)
print(artigo)
total_caracteres = artigo.pop('total_caracteres')
print(artigo)