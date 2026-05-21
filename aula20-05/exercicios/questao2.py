numeros = []

for i in range(10):
    numero = int(input(f"Digite um {i + 1} número"))
    numeros.append(numero)    

for i in range(9, -1, -1):
    print(numeros[i])    

  #numeros.sort(reverse=True)  
    #numeros.reverse  