"""
Exercício: 
Operação chamada crédito
"""
credito = {'123': 750, '789': 980}

score_123 = credito['123']
score_789 = credito['789']

print(score_123)
print(score_789)

### Elementos são atualizados pela sua chave. O elemento do cliente foi mudado sem ter que
### alterar o código.

credito['123'] = 435
print(credito)

### Para adicionar um novo elemento, basta criar um novo elemento chave-valor:

credito['456'] = 1000
print(credito)