""" contador = 0
while contador < 10:
    contador = contador + 1
    if contador == 1:
        print (contador, "Item limpo")
    else:
        print(contador, "Itens Limpos")
print("Fim da repetição do bloco while")

texto = input("Digite sua senha: ")
while texto != 'LetsCode':
    texto = input("Senha invalida, Tente novamente: ")

print("Acesso Permitido")"""

contador = 0
while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue
    else:
        print(contador, "Itens Limpos")
print("Fim da repetição do bloco while")