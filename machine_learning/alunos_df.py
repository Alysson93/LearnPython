import pandas as pd

# Criar série (vetor unidimensional)
impares = pd.Series([1, 3, 5, 7, 9])

alunos = {
    'nome': ['Alysson', 'Pereira', 'Assunção', 'Pessoa'],
    'nota': [5, 9, 3, 7],
    'aprovado': [False, True, False, True]
}

# Transformar dicionário em Data Frame:
alunos_df = pd.DataFrame(alunos)