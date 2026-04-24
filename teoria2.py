# nesse código, analisaremos a idade do usuário e falaremos
# se é maior de idade ou não
nome = input("Digite o seu nome:")
idade = int(input("Digite sua idade:"))
print("Olá" , nome, "! a sua idade é", idade)

# A estrutura decisão analisa uma comparação e executa o código
# com base na resposta. Para utilizarmos a estrutura de decisão, precisamos
# de comparadores, que são:

# - > maior
# - < menor
# - == igual
# - != diferente
# - >= maior ou igual
# - <= menor ou igual
# - ! não

# O comando de decisão é o if
# A sintaxe é:
# if comparação:
# E os itens a serem executados devem estar em um bloco identado
# if 20 > 30
#    print("Algo de errado não está certo")

if idade >= 18:
    print("Você é maior de idade!")
    print("Você pode comprar cigarro no Reino Unido")
    if idade >= 60:
        print("Você é idoso!")
        print("Você já pode pegar a carteirinha de estacionamento")
else:

    print("Você é menor de idade")
    print("Não pode comprar cigarro no Reino Unido")
    if idade < 18:
        print("Se tiver a intenção de comprar cigarro, recomendo que procure ajuda profissional")