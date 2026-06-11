print("Esse é o radar de velocidade da polícia da br 666")

v = int(input("Digite a sua velocidade: "))

if v <= 0:
    print("Erro")

elif v > 230:
    print("Erro")

elif v > 80:        
    print(f"Você foi multado por estar dirigindo a {v}km/h(excesso de velocidade)")
else:
    print(f"Você está a {v}km/h, dentro do limite permitido,\ncontinue sendo um cidadão responsável")    





