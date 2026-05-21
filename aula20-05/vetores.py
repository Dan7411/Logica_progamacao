# um vetor é uma variável que recebe diversos valores, em posições diferentes
alunos = ["Davi", "Daniel", "Wanchise", "Igor", "Nicoli", "Ian", "Natasha", "Fabio", ]
print("Formação original")
print(alunos)
#Para adicionar um valor ao final da lista, usamos a função append()
alunos.append("Antoni")
#Para remover um valor, usamos a função remove()
alunos.remove("Nicoli")
print("Adicionamos Antoni e removemos Nicole")


#Usamos a função len para verificar a quantidaded de itns em um vetor
#print(f"Há {len(alunos)} alunos presentes hoje!")
#Para iterar entre os itens do vetor, podemos usar a função
#for <váriavel item> in <variavel vetor>:

for aluno in alunos:
    #for = fazer variável só para for
    #print(f"Boa noite {aluno}")
    alunos.sort(reverse = True)
    print(alunos)






