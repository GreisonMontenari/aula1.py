"""
Métodos
São métodos nativos do Python que nos ajudam a trabalhar no dia a dia com listas
"""

juros = [0.05, 0.07, 0.02, 0.04, 0.08]
print(juros)

### inserir um elemento sem substituir: list.insert(index, val)
juros.insert(0, 0.10)
print(juros)

### inserir um elemento no fim da lista: list.append(val)
juros.append(0.09)
print(juros)

### remover um elemento pelo valor: list.remove(val)
juros.remove(0.1,)
print(juros)

### remover um elemento pelo índice: list.pop(val)
quinto_juros = juros.pop(2)
print(quinto_juros)

print(juros)
