"""
Conversão
Podemos converter strings em tipos numéricos e vice-versa.
"""

idade = 19 
print(type(idade))

idade = str(idade)
print(type(idade))

faturamento = 'R$ 35 mi'
print(faturamento)
print(type(faturamento))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))