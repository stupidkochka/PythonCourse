with open('rosalind_revc.txt') as file:
    a = file.read()
dna_1 = list(a)
for i in range(len(dna_1)):
    if dna_1[i] =='A':
        dna_1[i] = 'T'
        i+=1       
    elif dna_1[i] == 'T':
        dna_1[i] = 'A'
        i=+1
    elif dna_1[i] == 'G':
        dna_1[i] = 'C'
        i=+1
    elif dna_1[i] == 'C':
        dna_1[i] = 'G'
        i=+1
dna_2 = ''.join(dna_1)                   
print(dna_2[::-1])
