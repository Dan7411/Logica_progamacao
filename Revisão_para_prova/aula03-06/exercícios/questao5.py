print("Esse progama vai calcular sua média\ne dizer se foi aprovado, reprovado ou ficou em recuperação")

a = float(input("Digite sua primeira nota: "))
b = float(input("Digite sua segunda nota: "))

notas = {
    "n1" : "a",
    "n2" : "b",
    "m" : (
        (a + b) / 2
    ),
}
if notas["m"] >= 7:
    print(f"Você foi aprovado com média {notas['m']}")
elif notas["m"] >= 5:
    print(f"Você ficou de recuperação com média {notas['m']}")
else:
    print(f"Você foi reprovado com média {notas['m']}")        






