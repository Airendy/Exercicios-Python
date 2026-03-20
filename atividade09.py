#Leia o preço de um produto e imprima o preço com 10% de desconto.

preco = float(input("Preço: "))
desconto = preco * 0.10
preco_final = preco - desconto

print(preco_final)