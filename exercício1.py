numero_secreto = 3
tentativa = int(input("adivinhe o número: "))

while tentativa != numero_secreto:
    tentativa = int(input("Você errou, tente novamente!"))

print("Parabéns! Você acertou.")