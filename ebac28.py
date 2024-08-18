"""
Motivação
Exercicio: Você trabalha como analista de dados de mídias sociais
e precis adescobrir todas as hastags que alcançaram o top trending
do Twitter durante a semana. Você já conseguiu as hastags por dia 
da semana:
"""

hastags_seg = [ '#tiago', '#joao', '#bbb']
hastags_ter = ['#sarah', '#bbb', '#fiuk']
hastags_qua = ['#gil', '#thelma', '#lourdes']
hastags_qui = ['#rafa', '#fora', '#danilo']
hastags_sex = ['#juliete', '#neymar', '#bbb']

### Uma simples concatenação de listas fará com que a hastags #bbb,
### entre outras, apareça mais de uma vez.

#hastags_semana = hastags_seg + hastags_ter + hastags_qua + hastags_qui + hastags_sex
#print(hastags_semana)

hastags_semana = list(set(hastags_seg + hastags_ter + hastags_qua + hastags_qui + hastags_sex))
print(hastags_semana)
print(len(hastags_semana))   ### dessa forma removeu a duplicidade de lista ###