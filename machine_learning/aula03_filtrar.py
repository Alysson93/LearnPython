from alunos_df import alunos_df

print(alunos_df['nome']) # Filtra as colunas com índice especificado
print()


print(alunos_df.loc[[0]]) # Filtra a linha do índice especificado
print()

print(alunos_df.loc[[0, 1]]) # Filtra a linha dos índices especificados
print()

print(alunos_df.loc[1:3]) # Filtra índices do índice start até o stop
print()

aprovados = alunos_df.loc[alunos_df['aprovado'] == True] # Filtra as linhas a partir de uma condição
print(aprovados) 
print()

print(alunos_df) #
print()