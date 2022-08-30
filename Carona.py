valor_passagem = 4.30


valor_corrida = input("Digite o valor da corrida: ")
if float(valor_corrida) <= valor_passagem * 5:
    print("Pague a corrida")
elif float(valor_corrida) <= valor_passagem * 6:
    print("Espere um pouco mais e tente novamente")
else:
    print("Pegue o onibus")