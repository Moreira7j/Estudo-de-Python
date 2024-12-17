import os

mensagens= []

nome = input("Nome: ")

while True:

    #limpa o terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("________________")

    #obtendo texto

    texto = input("Escreva: ")
    if texto == "fim":
        break

    #adicionando a mensagem

    mensagens.append({
        "nome": nome,
        "texto": texto
    })
