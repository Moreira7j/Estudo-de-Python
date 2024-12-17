#Soma de números

numero = int(input("Digite até que número é desejado: "))
soma=0

for i in range(1, numero + 1):   #pode se usar a fórmula matemática que seria numero * (número + 1) / 2
    soma += i

print("A soma de todos os números são: ", soma)