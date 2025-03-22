# Resolução 01
vetor = []
vetor_par = []
vetor_impar = []

for i in range(20):
    num = int(input("Digite Um Número: "))
    vetor.append(num)
    if vetor[i] % 2 == 0:
        vetor_par.append(vetor[i])
    else:
        vetor_impar.append(vetor[i])

print(f"Vetor completo: {vetor} \nImpares: {vetor_impar} \nPares: {vetor_par} ")

# Resolução 02
numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nVetor de Números:", numeros)
print("Vetor de Números Pares:", pares)
print("Vetor de Números Ímpares:", impares)
