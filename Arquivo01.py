arquivo = open('dom_casmurro_cap_1.txt', 'r')
texto = arquivo.read()
print(texto)
arquivo.close()

arquivo = open('dom_casmurro_cap_1.txt', 'r')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

arquivo = open('dom_casmurro_cap_1.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

with open('dom_casmurro_cap_1.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto)

with open('copiateste.txt', 'w') as arquivo:
    arquivo.write('Essa é a primeira linha que eu escrevi usando Python\n')
    arquivo.write('Essa é a segunda linha que eu escrevi usando Python\n')


with open('copiateste.txt', 'a') as arquivo:
    arquivo.write('Essa é a terceira linha que eu escrevi usando Python\n')

with open('copiateste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')
