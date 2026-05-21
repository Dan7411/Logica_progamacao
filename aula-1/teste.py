nota1 = int(input("Digite uma nota 1:"))
nota2 = int(input("Digite uma nota 2:"))
nota3 = int(input ("Digite uma nota 3:"))

#fora do while

round_de_sangramento = 3

while round_de_sangramento:

    dano_p1 = 10
    print(f"nome do personagem usou tal coisa para infligir sangramento")
    print(f"personagem dois) receberá dano de dano por rounds_de_sangramento/ turno")
    
    if round_de_sangramento > 0:
        dano_p1 +=10
        print("[ SANGRAMENTO ] +10 de dano adicionado")
        round_de_sangramento -= 1




















