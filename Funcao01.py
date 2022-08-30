def piscina(*infos):
    vol = infos[0]*infos[1]*infos[2]
    return vol

volume = piscina(5, 4, 5)

print('O volume é: ', volume)

def piscina(prof, largura, comprimento):
    vol = prof*largura*comprimento
    return vol

lista = [5, 4, 5]

volume = piscina(*lista)

print('O volume é: ', volume)

def piscina(prof, **infos):
    vol = prof*infos['largura']*infos['comprimento']
    return vol

volume = piscina(5, largura=4, comprimento=5)

print('O volume é: ', volume)

def piscina(prof, largura=4, comprimento=5):
    vol = prof*largura*comprimento
    return vol

infos = {'largura': 10, 'comprimento': 20}

volume = piscina(5, **infos)

print('O volume é: ', volume)