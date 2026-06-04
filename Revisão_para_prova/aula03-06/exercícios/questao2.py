print("Bem vindo a esse protótico de calculadora,\natualmente só exibe o dobro e a metade de qualquer valor")

v = float(input("Digite o valor: "))

valores = {
"d" : v * 2,
"m" : v / 2
}

print(f"o dobro de {v} é {valores["d"]} e a metade é {valores["m"]}")

