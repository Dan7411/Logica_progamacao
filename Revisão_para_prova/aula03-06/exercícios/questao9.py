import time

print("OBS:Letras somente maiúsculas")

a = True
t = 1

while True:
  
  senha = (input("\nDigite a senha: "))
  
  if senha in ["SENAI123"]:
      time.sleep(1)
      print("Senha confirmada, entrada permitida.")        
      break

  elif senha not in ["SENAI123"]:
   print(f"\nSenha inválida")
   t += 1
   if t > 3:
       time.sleep(1)
       print("\nVocê foi além do número de tentativas permitidas,\nagora o progama será encerrado.")
       break

  