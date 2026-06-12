import time
saldo = 1000.0

print("Opções:\n1-Verificar saldo\n2-Depositar\n3-Sacar\n4-Sair do sistema ")

while True: 
 
 time.sleep(1)
 opcao = int(input("\nDigite sua opção: "))
   
 match opcao:
   case "1":
     
     print(f"Conta acessada, saldo de {saldo:.2f} ")

   case "2":
     
     v = float(input("Valor que deseja depositar em sua conta: "))
     saldo = saldo + v
     print("Valor depositado com sucesso.")

     if v <= 0:
       print("Erro, seu depósito foi negativo")
   
   case "3": 
     d = float(input("Digite o valor que deseja sacar: "))
     saldo = saldo - d    
     print("Valor sacado com sucesso.")
     if d > saldo:
       print("Erro, você não tem saldo o bastante.")
  
   case "4":
     print("Tem certeza?")
     s = int(input("Se sim, digite 0: "))
     if s == 0:
       print("Saindo do sistema.")
       break
     
   case _:
     print("Opção inválida, tente novamente.")
              





