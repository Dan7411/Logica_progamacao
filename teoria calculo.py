# Pedir 3 notas e armazenado em variáveis diferentes

nota1 = float(input("Digite uma nota 1:"))
nota2 = float(input("Digite uma nota 2:"))
nota3 = float(input ("Digite uma nota 3:"))

soma = nota1 + nota2 + nota3 
média = soma/3

print("A média das notas é",média)
if média > 7.0:
 print("Você foi aprovado")
 ota1 = float(input("Digite uma nota 1:"))
nota2 = float(input("Digite uma nota 2:"))
nota3 = float(input ("Digite uma nota 3:"))

soma = nota1 + nota2 + nota3 
média = soma/3

print("A média das notas é",média)
if média > 7.0:
 print("Você foi aprovado")    
 print("Pois a média mínima é 7.0")
else:
 # elif, else + if
 print("Você foi reprovado")
 print("Pois a média mínima é 7.0")