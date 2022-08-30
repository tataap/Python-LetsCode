import csv
from typing import List

with open('brasil.covid1.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    heador = next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

