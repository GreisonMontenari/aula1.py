"""
Interpolação básica de strings
s - corda
D e I - Int
f - flutuador
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Greison'
preco = 1000.65897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))