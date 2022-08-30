dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km2': 1521,
    'populacao_milhoes': 12.18,
}

print(type(dados_cidade))

print(dados_cidade)

dados_cidade['pais'] = 'Brasil'

print(dados_cidade)

print(dados_cidade['nome'])

dados_cidade['area_km2'] = 1500
print(dados_cidade)

dados_cidade1 = dados_cidade.copy()
dados_cidade1['nome'] = 'Santos'
dados_cidade1['area_km2'] = 281.033
dados_cidade1['populacao_milhoes'] = 0.44

print(dados_cidade1)

novos_dados = {
    'populacao_milhoes' : 15,
    'fundacao' : '25/01/1554',
}
dados_cidade.update(novos_dados)
print(dados_cidade)
print(dados_cidade.get('prefeito'))
print(' ')
print(dados_cidade.keys())
print(' ')
print(dados_cidade.values())
print(' ')
print(dados_cidade.items())

d