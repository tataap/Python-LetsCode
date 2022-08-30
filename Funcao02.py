'''def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media'''


def calcula_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)
    return media + margem

resultado = calcula_media(10, 9, 8, margem=0.3)
print(resultado)

def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome='Taís', sobrenome='Silva')