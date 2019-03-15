with open ('1.txt') as file: #здесь должны быть имнна файлов с rosalind
    a = file.read()
with open ('2.txt') as file:
    b = file.read()
hamming_distance = 0
for i in range(len(a)):
    if a[i]==b[i]:
        hamming_distance += 1
        i += 1
    else:
        i += 1

print ('N = {}'.format(hamming_distance))        
    
    