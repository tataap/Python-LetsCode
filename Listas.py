nomes_paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']
print(nomes_paises)

print("Tamanho da Lista: ", len(nomes_paises))

print("País: ", nomes_paises[4])
print("País: ", nomes_paises[-1])

nomes_paises[4] = 'Colombia'
print("País: ", nomes_paises[4])
print(nomes_paises)

print(nomes_paises[1:3])
print(nomes_paises[1:-1])
print(nomes_paises[:3])
print(nomes_paises[2:])
print(nomes_paises[::2])
print(nomes_paises[:])
print(nomes_paises[::-1])

print('Brasil' in nomes_paises)
print('Canadá' not in nomes_paises)

lista_capitais = []

lista_capitais.append('Brasilia')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')
lista_capitais.append('Otawa')

lista_capitais.remove('Buenos Aires')
print(lista_capitais)

removido = lista_capitais.pop(2)
print(lista_capitais, removido)

lista_capitais.insert(1, 'Buenos Aires')
lista_capitais.insert(2, 'Bogotá')
print(lista_capitais)