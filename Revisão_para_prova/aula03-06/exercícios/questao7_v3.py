import time
print("Você digitará um número entre 1 e 10\npara ser exibida a tabuada do 1 até 10")
n = int(input("Digite um número inteiro entre 1 e 10: "))
nn = int(input("Digite até qual tabuada será multiplicada: "))
if n < 1:
 print("Erro") 
elif n > 10:
 print("Erro")

for i in range(0,11):
 print(f"{n} x {i} = {n * i}")








