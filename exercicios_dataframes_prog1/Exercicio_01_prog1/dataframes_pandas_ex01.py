"""
1) Baixar o arquivo 'github-ranking-2022-12-07.csv' e implementar as seguintes funções:
● Gerar um csv eliminando as linhas cuja coluna “language” seja diferente de Python
● Gerar um csv com os 50 repositórios Python com mais stars
● Gerar um csv com os 50 repositórios Python com mais forks
"""

import pandas as pd

def only_python_language(df):
    python_language = list(df['language'] == 'Python')
    new_df = df.loc[python_language]
    new_df.to_csv('only_python_language.csv')

def python_repositories_with_more_stars(df):
    python_language = list(df['language'] == 'Python')
    df = df.loc[python_language]
    df_sort = df.sort_values(by = 'stars', ascending = False)
    more_stars = df_sort.head(n = 50)
    more_stars.to_csv('python_repositories_with_more_stars.csv')

def python_repositories_with_more_forks(df):
    python_language = list(df['language'] == 'Python')
    df = df.loc[python_language]
    df_sort = df.sort_values(by = 'forks', ascending = False)
    more_forks = df_sort.head(n = 50)
    more_forks.to_csv('python_repositories_with_more_forks.csv')

df = pd.read_csv('github-ranking-2022-12-07.csv')

# Tratamento de dados

dados = []

for cont in range(df.shape[0]):
    d = df.iat[cont,0].split(',')
    dados.append(d)

# Criação de um novo DataFrame

colunas = [
    'repo_name', 
    'stars', 
    'forks', 
    'language', 
    'repo_url', 
    'username', 
    'issues',
    'last_commit', 
    'description'
]

remover_colunas = [9,10,11,12,13,14,15,16,17,18,19,20,21]

df = pd.DataFrame(data = dados)
df.drop(columns = remover_colunas, inplace = True)
df.columns = colunas
df.drop_duplicates()

only_python_language(df)
python_repositories_with_more_stars(df)
python_repositories_with_more_forks(df)
print('Arquivos criados!')