#Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.

salario = float(input("Salário: "))
percentual = float(input("Percentual de aumento: "))

novo_salario = salario + (salario * percentual / 100)

print(f"Novo salário: {novo_salario:.2f}")
