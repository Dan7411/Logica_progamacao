import time
saldo = 1000.0

print("Opções:\n1 Verificar saldo\n2 Depositar dinheiro\n3 Sacar dinheiro\n4 Sair do sistema ")

while True: 
 
 time.sleep(1)
 opcao = input("\nDigite sua opção: ")
   
 match opcao:
   case "1":
     print("Conta acessada, saldo de " , saldo)

   case "2":
     v = float(input("Valor que deseja depositar em sua conta: "))
     saldo = saldo + v
    
   case "3":
     d = float(input("Digite o valor que deseja sacar: "))
     saldo = saldo - d    

   case "4":
     print("Tem certeza?")
     s = int(input("Se sim, digite 0: "))
     if s == 0:
       print("Saindo do sistema.")
       break
     
    
              





