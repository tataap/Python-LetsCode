empresa = 'Google'
print(empresa)

empresa = "Google"
print(empresa)

empresa = "Let's Code"
print(empresa)

frase = "O professor Pierto da Let's Code disse: \"Hoje a pizza é por minha conta\""
print(frase)

nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

cabecalho = "                MENU PRINCIPAL               "
print(cabecalho.strip())

nome_cidade = "rIo dE jaNEirO"

print(nome_cidade.title())
print(nome_cidade.capitalize())
print(nome_cidade.lower())
print(nome_cidade.upper())

"""nome_cidade = input('Que cidade no Brazil é conhecida como cidade maravilhosa? ')
nome_cidade = nome_cidade.strip()

while nome_cidade.lower() != 'rio de janeiro':
    print('Tente de novo, vai')
    nome_cidade = input('Que cidade no Brazil é conhecida como cidade maravilhosa? ')

print('Booa, Campeão!')"""

mensagem = "Você viu o que o Pietro disse na sala ontem?"
fui_citado = "Pietro" in mensagem
print(fui_citado)