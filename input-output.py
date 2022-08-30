salario_mensal = input("Digite o valor do seu salário mensal: ")
salario_mensal = float(salario_mensal)

gasto_mensal = input("Digite o valor do gasto mensal médio: ")
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print("O montante que pode ser economizado no final do ano é: ", montante_economizado)