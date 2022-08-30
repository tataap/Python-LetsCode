import csv

with open('users.csv', 'w', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Taís', ' Silva', ' tais_ap12@hotmail.com', ' Feminino'])
    escritor.writerow(['Marcela', ' Silva', ' marcelaa.cardoso@gmail.com', ' Feminino'])

with open('users.csv', 'r') as arquivo_users:
    print(arquivo_users.read(), end='')

header = ['nome', 'sobrenome']
dados = []
opt = input('O que deseja fazer?\n - Cadastrar\n0 - Sair\n')
while opt != '0':
    nome = input('Qual seu nome?')
    sobrenome = input('Qual seu sobrenome?')
    dados.append([nome, sobrenome])
    opt = input('O que deseja fazer?\n - Cadastrar\n0 - Sair\n')

print(dados)

with open('users.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)