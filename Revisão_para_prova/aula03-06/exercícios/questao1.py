informacoes = {}

print("Bem vindo\nEsse é a verificação do seu cracha,\na seguir, digite algumas informações")
 
informacoes["nome"] = input("Digite o seu nome: ").upper()

informacoes["idade"] = int(input("Digite a sua idade: ")) 
 
informacoes["cidade"] = input("Digite a sua cidade natal: ").upper()
 


print("\nNome:",(informacoes['nome']))
print("Idade:",(informacoes['idade']))
print("Cidade natal:",(informacoes['cidade']))
