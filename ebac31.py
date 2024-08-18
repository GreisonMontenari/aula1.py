"""
Podemos criar dicionários compostos.
Quando esse dicinário é criado de forma correta ele se torna
uma ferramenta poderosa.
"""

cadastro = {
    'greison': {
        'nome': 'Greison Montenari',
        'ano_nascimento': 1987,
        'pais': {
            'pai':{
                'nome': '<nome-do-pai> Ferreira',
                'ano_nascimento': 1971
            },
            'mae': {
                'nome': '<nome-da-mae> Montenari',
                'ano_nascimento': 1973
            },
            
        }
    }
}

print(cadastro)

