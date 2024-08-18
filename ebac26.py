"""
Método de manipulaçao de conjuntos
São métodos nativos do Python que nos ajudam a trabalhar 
no dia a dia com conjuntos.
"""

cursos = {'Exatas', 'Humanas', 'Biológica'}
print(cursos)

### inserir um elemento no conjunto: set.add(val)
cursos.add('Saúde')
print(cursos)

### remover um elemento do conjunto: set.remove(val)
cursos.remove('Saúde')
print(cursos)