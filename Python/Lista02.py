# Resolução 01
vetor = []
for i in range(10):
    num = int(input("Digite Um Número: "))
    vetor.append(num)

for h in range(len(vetor)//2):
    a = vetor[h]
    vetor[h] = vetor[-h-1]
    vetor[-h-1] = a

print(vetor)

# Resolução 02
vetor = []

for i in range(10):
    numero = float(input(f"Digite o número {i+1}: "))
    vetor.append(numero)

print("Números na ordem inversa:")
for i in range(9, -1, -1):
    print(vetor[i])
