"""Break / continue
Break ele é responsável pela quebra do loop,
break sempre que tiver presente ele quebra o loop
e continua a execução do código.
Estrutura que permite a quebra ou o avanço
de um laço de repetição.
"""

numeros = [361, 553, 194, 13, 510, 33, 135]

for numero in numeros:

    if numero % 2 == 0:
        print(f'O numero {numero} é par')
        break
    else:
        print(f'O numero {numero} é impar')