# Resolução 01
vetor = []
for i in range(10):
    char = input("Digite Uma letra: ")
    vetor.append(char.upper())

soma = 0
vogais = ["A", "E", "I", "O", "U"]
for i in range(len(vetor)):
    if vetor[i] not in vogais:
        soma += 1
print(f"Número de consoantes é {soma} ")

# Resolução 02
def eh_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return caractere in consoantes

def main():
    vetor = []
    consoantes_lidas = []

    for i in range(10):
        caractere = input("Digite um caractere: ")
        vetor.append(caractere)
        if eh_consoante(caractere):
            consoantes_lidas.append(caractere)

    print(f"Quantidade de consoantes lidas: {len(consoantes_lidas)}")
    print(f"As consoantes digitadas foram: {', '.join(consoantes_lidas)}")

if __name__ == "__main__":
    main()
