nu = int(input("Digite qualquer número inteiro(número sem vírgula): "))

if nu % 2 == 0:
   print(f"{nu} é um número par.")
   if nu > 10:
       print("È maior que 10")
else:
    print(f"{nu} é um número ímpar")    
    if nu < 5:
        print("È menor que 5")




