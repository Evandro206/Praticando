# Resolução 01
vetor = []
for i in range(4):
    num = float(input("Digite Um Número: "))
    vetor.append(num)

soma = 0
for i in range(len(vetor)):
    soma = soma + vetor[i]

print("Notas: ", vetor)
print(f"Média: {soma / len(vetor)}")

# Resolução 02
notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:", notas)
print(f"Média: {media:.2f}")