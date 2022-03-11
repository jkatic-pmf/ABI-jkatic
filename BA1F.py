#BA1F

dna = input()

zbroj = 0
min_v = 0
min_i = []

for i in range(len(dna)):
    if dna[i] == 'C':
        zbroj -= 1
    elif dna[i] == 'G':
        zbroj += 1
        
    if min_v > zbroj:
        min_v = zbroj
        min_i = [i+1]
    elif min_v == zbroj:
        min_i.append(i+1)

rez = ''
for el in min_i:
    rez += str(el) + ' '

print(rez)
