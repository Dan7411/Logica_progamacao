print("|-----------------------|")
print("       Calculadora       ")
print("|-----------------------|")
print("Essa caculadora, faz todas as operações")
print("a partir de dois números que você informar")
print("Digite o valor correspondente ao cálculo que você quer fazer")
print("O que você quer fazer")
print("1 - 4 operações")
print("2 - Média de 3 valores")
print("3 - Fómula de Bháskara")
opcao = int(input("Digite a opcão: "))
match opcao:
    case 1:
        n1=float(input("Digite o primeiro número:"))
        n2=float(input("Digite o segundo número:"))
        adicao = n1 + n2
        print(f"A adicao resulta em: {adicao}")
        subtracao = n1 - n2
        print(f"A subtração resulta em: {subtracao}")
        multiplicacao = n1 * n2
        print(f"A multiplicação resulta em: {multiplicacao}")
        if n2 != 0:
            divisao = n1 / n2
            print(f"A divisão resulta em: {divisao}")
        else:
            print("A divisão não pode ser feita")   
# exclamação e igual signifa diferente diferente
# igual e igual signifa igual

    case 2:
        n1 = float(input("Digite seu número:"))
        n2 = float(input("Digite seu número:"))
        n3 = float(input("Digite seu número:"))
        resultado = (n1 + n2 + n3) / 3
        print(f"Resulta em média {resultado}")
    case 3:
        print("Fómula de Bháskara")        



