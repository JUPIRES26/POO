soma = 0

print("digite números para somar. Digite 0 para encerrar")

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    soma += numero

print("A soma total é: ", soma)