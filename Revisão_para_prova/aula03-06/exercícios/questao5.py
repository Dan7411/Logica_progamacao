print("Esse progama vai calcular sua média\ne dizer se foi aprovado, reprovado ou ficou em recuperação")

a = float(input("Digite sua primeira nota: "))
b = float(input("Digite sua segunda nota: "))

notas = {
    "n1" : "a",
    "n2" : "b",
    "m" : (
        (a + b) / 2
    ),
    "s1" : "aprovado",
    "s2" : "reprovado",
    "s3" : "recuperação"
}
if notas["m"] >= 7:
    print(f"Você foi {notas['s1']} com média {notas['m']}")
elif notas["m"] >= 5:
    print(f"Você ficou de {notas['s3']} com média {notas['m']}")
else:
    print(f"Você foi {notas['s2']} com média {notas['m']}")        






