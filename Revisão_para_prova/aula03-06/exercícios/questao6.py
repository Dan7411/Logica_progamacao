import time

t = int(input("Número: "))

print("Este é um cronômetro")

while True:
  print(f"\n {t}")
  time.sleep(1)
  t -= 1
  if t < 1:
   print("\nFim do tempo")
   break










