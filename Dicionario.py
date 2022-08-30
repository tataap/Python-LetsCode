dicionario = {}

# O dicionário não possui um "append".
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))


# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)
# Saída: {'cat': 'gato', 'dog': 'cão', 'mouse': 'rato'}

# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)


if 'cat' in dicionario:
    print('cat existe!') # Sim
if 'bird' in dicionario:
    print('bird existe!') # Não
if 'gato' in dicionario:
    print('gato existe!') # Não

'''
Também podemos utilizar as funções .keys() e .values() para obter listas
com apenas as chaves ou apenas os valores do dicionário.
'''
chaves = dicionario.keys()
print(chaves)
# Saída: dict_keys(['cat', 'dog', 'mouse'])

valores = dicionario.values()
print(valores)
# Saída:dict_values(['gato', 'cão', 'rato'])

# Já a função .items(), retorna uma lista de tuplas (chave, valor) de um dicionário

itens = dicionario.items()
print(itens)
# Saída:dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])