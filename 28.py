valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra > 500:
    desconto = 0.10 
elif valor_compra > 100:
    desconto = 0.05
else:
    desconto = 0.0 

valor_final = valor_compra * (1 - desconto)

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Valor a pagar: R$ {valor_final:.2f}")