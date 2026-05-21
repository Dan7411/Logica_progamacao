import time
import random

print("#### Jogo da adivinhação ####")


print("Estou pensando em um número...")

time.sleep(2)


print("Pensei!")
print("Você poderá tentar adivinhar ele")
# para i em um intervalo de 1 até 1 até 4
#for i in range(1,4):
    #print(f"essa é sua {i} tentativa")
  #  tentativa = int(input("Digite um valor entre 0 e 10: "))

   # if tentativa == numero:
    #    print("Parábens! Você acertou o número.")
    #else:
     #   print("Você errou!")
acertou = False
num_tentativa = 0
numero = random.randint(0,10)

while acertou == False:
    num_tentativa += 1
    print(f"Essa é a {num_tentativa} tentaiva")
    tentativa = int(input("Digite um valor entre 0 e 10: "))
    
    if tentativa == numero:
        print("Parabéns, você acertou!")
        acertou = True
    else:
        print("Você errou")
        if num_tentativa > 10:
            print("### Você é burro! Rsrsrsrsrs! ###")    












