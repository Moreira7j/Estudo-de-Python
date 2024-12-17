#exemplo de saida e entrada de dados

# nome = input("digite o seu nome: ")
# idade = int(input("digite sua idade: "))
# peso = float(input("digite o seu peso: ")) 

# print(type(nome))
# print(type(idade))
# print(type(peso))



#EXEMPLO DE OPERAÇÕES BÁSICAS

# soma = 2+2
# multiplicação = 2*2
# divisão= 30/3
# potenciação= 7**2

# print("soma: ", soma)
# print("multiplicação: ",multiplicação)
# print("divisão: ", divisão)
# print("potenciação: ",potenciação)


#CONDICIONAIS

# idade = int(input("digite sua idade: "))
# idadeP = 18

# if idade >= idadeP:
#     print("Acesso Liberado")
# else:
#     print("Acesso negado")



# salario = float(input("DIgite o seu salário: "))

# if salario <=3000:
#     print("programador junior")
# elif salario > 3000 and salario <= 6000:
#     print("Programador pleno")
# elif salario > 6000 and salario <= 15000:
#     print("Programador senior")
# else:
#     print("gerente de Projetos")


#LISTAS

# listasN= [10, 2, 3] 

# listasN[0]= 2 #isso serve para manipular o valor das posições

# print(listasN[0])  # o numero de posições começa do numero 0 


# listav= []

# listav.append("salva rapazeada")
# print(listav)

# lista= [10, 2 , 5 , 6]

# print("Total: ", len(lista))
# print("Maior valor: ", max(lista))
# print("Menor valor: ", min(lista))


#REPETIÇÃO FOR

# for x in range(5):
#     print(x)


# notas=[]

# for x in range(3):
#     codigo= input("Digite o RM: ")
#     nota= float(input("Nota: "))
#     resultado = [codigo, nota]
#     notas.append(resultado)

# print("Quantidade de notas", len(notas))

# for n in notas:
#     codigo=n[0]
#     nota=n[1]
#     print("O RM:", codigo, "Tirou nota: ", nota)



#REPETIÇÃO WHILE

# notas= []

# contador = 1

# while contador <= 5:
#     codigo= input("Digite o RM: ")
#     nota= float(input("Nota: "))
#     resultado = [codigo, nota]
#     notas.append(resultado)

#     contador += 1 

# print(" A quantidade de notas: ", len(notas))



#Dicionario

pessoa= {
    
    "nome": "Programador",      #dentro de uma variável podemos ter varios atributos
    "idade": 17,
    "peso": 60
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])
