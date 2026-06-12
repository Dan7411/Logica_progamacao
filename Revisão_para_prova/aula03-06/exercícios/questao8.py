import time
valor =[]

i = 1

p = 1
while True:
 v = float(input(f"Digite o valor do produto {p}: "))
 p += 1
 valor.append(v)
 if v == 0:
  break
  


print("A soma dos valores é R$",sum(valor))
time.sleep(1)

for produto in valor:
  if produto != 0:
   print("\nO resultado da sua compra: ")

   print(f"Valor do produto {i}: {produto}")
   time.sleep(1)
   i +=1
   





