print("Bem vindo a esse protótico de calculadora,\natualmente só exibe o dobro e a metade de qualquer valor")

v = float(input("Digite o valor: "))

valores = {
"d" : v * 2,
"m" : v / 2,
"x" : v *3
}

print(f"o dobro é {valores["d"]},\nseu triplo é {valores["x"]}\ne a metade é {valores["m"]}")

