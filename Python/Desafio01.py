def DNAtest(string):
    string = string.upper() # String recebe String maiuscula
    arr = list(string) # Arr recebe String em forma de lista
    dna = list('ATGC') # Dna é uma lista com as letras padão de um dna
    for letra in arr:
        if letra not in dna: # verifica se a letra de Arr está em Dna
            return False
    return True

dna1 = "AGCT"
dna2 = "AGXT"
dna3 = "atgctagc"

print(f"DNAtest('{dna1}') -> {DNAtest(dna1)}")
print(f"DNAtest('{dna2}') -> {DNAtest(dna2)}")
print(f"DNAtest('{dna3}') -> {DNAtest(dna3)}")
