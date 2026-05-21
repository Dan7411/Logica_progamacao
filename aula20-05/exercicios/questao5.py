numeros = []
pares = []
impares = []

for i in range(0,20):
    numero = int(input("Digite um numero inteiro:  "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)








