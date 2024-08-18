"""
Formatação básica de strings
s - corda
d - int
f - flutuador
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Bandeiras de conversão - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{-1000.5454878765656565:,.1f}')