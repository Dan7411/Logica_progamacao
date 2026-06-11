a = 1

import time
print("Você digitará um número entre 1 e 10\npara ser exibida a tabuada do 1 até 10")
n = int(input("Digite um número inteiro entre 1 e 10: "))
nn = int(input("Digite até qual tabuada será multiplicada: "))
if n < 1:
 print("Erro") 
elif n > 10:
 print("Erro")


else:
   while True:
    r = n * a
    print(f"{n} * {a} = {r}")
    a += 1
    time.sleep(1)
    if a >= nn:
     break



