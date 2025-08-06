pessoa = {'name':'Mercuri', 
          'old':20, 
          'year_formation':2026, 
          'Tools':['python', 'PowerBI', 'Excel', 'ETL'], 
          'Brazilian':True, 
          'musics':['Where have you been', 'dont stop music', 'mesma fita'], 
          'God not exist':False}

# Imprima na tela o valor equivalente a chave "hobby"
print(pessoa['musics'])

# Imprima na tela uma lista apenas com os valores do dicionário
print(pessoa.values())


# Imprima na tela uma lista apenas com as chaves do dicionário
print(pessoa.keys())


# Insira um novo par chave-valor no dicionário
pessoa['ETL'] = 'PowerBI'
print(pessoa)