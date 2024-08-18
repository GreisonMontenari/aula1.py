"""
Métodos
São métodos nativos do Python que nos ajudam a trabalhar
no dia a dia com strings:
"""

### upper(deixa tudo em letras maiusculas) string.upper()

#endereco = 'Avenida Paulista, 1811, São Paulo, São Paulo, Brasil.'
#print(endereco.upper())

### posicao: string.find(substring)

endereco = 'Avenida Paulista, 1811, São Paulo, São Paulo, Brasil.'
posicao = endereco.find('Greison') ### Meu nome nao será encontrado, se colocar outra frase da string aí dará certo
print(posicao)

### substituição: string.replace(antigo, novo)
print(endereco.replace('Avenida', 'Av'))