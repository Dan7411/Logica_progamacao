
frutas = ["Banana","Maçã","Tomate","Laranja","Melâcia"]
verduras = ["Alfacwe", "Repolho", "Acelga"]

print("Bem vindo ao montador de saladas!")
print("aqui você poderá montar sua salada favorita!")

print("Primeiramente, você quer ver as frutas ou verduras?")
print("1 - Frutas  |  2 - Verduras")
opcao = input("Escolha dentre as opções (1 ou 2): ")

match opcao:
    case "1":
        for index,fruta in enumerate(frutas):
            print(f"Frutas #{index+1}: {fruta}")
    case "2":
        for index,verdura in enumerate(verduras):
            print(f"Verdura #{index+1}: {verdura}")


index_ingrediente = int(input("Digite o número do ingrediente que você deseja: "))-1

ingrediente = ""

if opcao == "1":
    ingrediente = frutas[index_ingrediente]

elif opcao == "2":
    ingrediente = verduras[index_ingrediente]







