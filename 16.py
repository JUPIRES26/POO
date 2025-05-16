preço = float(input("digite o valor do preço:"))
desconto_percentual = float(input("digite o valor do desconto percentual:"))

valor_desconto = preço * (desconto_percentual / 100)

preço_final = preço - valor_desconto

print("o preço com desconto é:", round(preço_final, 2))