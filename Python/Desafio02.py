def DNArna(string):
    string = string.upper()
    arr = list(string)
    dna = list('ATGC')
    for letra in arr:
        if letra not in dna:
            return False
    for i in range(len(arr)):
        if arr[i] == 'T':
            arr[i] = 'U'
    return ''.join(arr)

dna1 = "AGCT"
dna2 = "AGXT"
dna3 = "atgctagc"

print(f"DNArna('{dna1}') -> {DNArna(dna1)}")
print(f"DNArna('{dna2}') -> {DNArna(dna2)}")
print(f"DNArna('{dna3}') -> {DNArna(dna3)}")