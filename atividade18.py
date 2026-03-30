#Leia um nome e uma nota (float), com uma casa decimal, e imprima:
#Aluno <nome> ficou com nota <nota>

nome = input("Nome do aluno: ")
nota = float(input("Nota: "))

print(f"Aluno {nome} ficou com nota {nota:.1f}")
