import time
print("Você digitará um número entre 1 e 10\npara ser exibida a tabuada do 1 até 10")
n = int(input("Digite um número inteiro entre 1 e 10: "))

if n < 1:
 print("Erro") 
elif n > 10:
 print("Erro")

else:
  
  tabuada = {
  "t1" : n * 1,
  "t2" : n * 2,
  "t3" : n * 3,
  "t4" : n * 4,
  "t5" : n * 5,
  "t6" : n * 6,
  "t7" : n * 7,
  "t8" : n * 8,
  "t9" : n * 9,
  "t10" : n * 10
  
  }
  
  
  if n < 1:
   print(f"\n{n}.1 = {tabuada['t1']} ")
   time.sleep(1)
   print(f"{n}.2 = {tabuada['t2']} ")
   time.sleep(1)
   print(f"{n}.3 = {tabuada['t3']} ")
   time.sleep(1)
   print(f"{n}.4 = {tabuada['t4']} ")
   time.sleep(1)
   print(f"{n}.5 = {tabuada['t5']} ")
   time.sleep(1)
   print(f"{n}.6 = {tabuada['t6']} ")
   time.sleep(1)
   print(f"{n}.7 = {tabuada['t7']} ")
   time.sleep(1)
   print(f"{n}.8 = {tabuada['t8']} ")
   time.sleep(1)
   print(f"{n}.9 = {tabuada['t9']} ")
   time.sleep(1)
   print(f"{n}.10 = {tabuada['t10']} ")
   time.sleep(1)
   
  
  


