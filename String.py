frase = 'uma FRASE'

print(frase[0])
print(frase[1])
print(frase[2])

tamanho = len(frase)
print("A frase possui", tamanho, "caracteres")

listafrase = list(frase)
print(listafrase)

stringfinal = '-py'.join(listafrase)
print(stringfinal)

s1 = frase.capitalize() # 1a letra maiúscula, restante minúscula
s2 = frase.title() # todo início de palavra em maiúscula, resto minúscula
s3 = frase.upper() # string inteira em maiúscula
s4 = frase.lower() # string inteira em minúscula
s5 = frase.replace('F', 'C') # substitui a primeira substring pela segunda

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print('String original:', frase)

quebra1 = frase.split(' ') # quebra a frase no caractere espaço em branco
quebra2 = s3.split('A') # quebra a frase em maiúsculas no caractere 'A'

print(quebra1)
print(quebra2)

frase = 'uma\nFRASE'
print(frase)

frase = 'uma\n\tFRASE'
print(frase)

frase = 'uma\\FRASE'
print(frase)