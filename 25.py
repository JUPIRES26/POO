a = float(input("digite o coeficiente a:"))
b = float(input("digite o coeficiente b:"))
c = float(input("digite o coeficiente c:"))

X1 = (-b + ((b * b - 4 * a * c) ** 0.5)) / (2 * a)
X2 = (-b - ((b * b - 4 * a * c) ** 0.5)) / (2 * a)

print(f"resultado 'x1' : {round(X1, 2)} \n resultado 'X2' : {round(X2, 2)} ")