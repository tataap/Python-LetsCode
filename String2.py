dicionario = {}

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))


dicionario['dog'] = 'cão'
print(dicionario)


dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)


if 'cat' in dicionario:
    print('cat existe!')
if 'bird' in dicionario:
    print('bird existe!')
if 'gato' in dicionario:
    print('gato existe!')


chaves = dicionario.keys()
print(chaves)

valores = dicionario.values()
print(valores)

itens = dicionario.items()
print(itens)
