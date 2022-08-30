arquivocriado = open("criado.txt", "w")
arquivocriado = open("teste.txt", "w")

arquivolido = open("teste.txt", "r")

dados = arquivolido.read()
print(dados)

arquivocriado.write("linha 1")
arquivocriado.write("linha 2")
arquivocriado.write("linha 3")

arquivocriado.close()
arquivolido.close()

with open('teste.txt', 'r') as arquivolido:
   dados = arquivolido.read()
   print(dados)

with open('teste.txt', 'r') as arquivolido:
   linha = arquivolido.readline()
   while linha != '':
       print(linha, end='')
       linha = arquivolido.readline()


# OU

with open('teste.txt', 'r') as arquivolido:
    for linha in arquivolido:
        print(linha, end='')

with open('teste.txt', 'r') as arquivolido:
    with open('copiateste.txt', 'w') as arquivocriado:
        for linha in arquivolido:
            arquivocriado.write(linha)