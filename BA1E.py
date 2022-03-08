#BA1E

import re

genome = input()
k = int(input())
L = int(input())
t = int(input())

gen_niz = []

for i in range(len(genome)-k):
    temp_k = genome[i:i+k]
    if temp_k in gen_niz: continue

    matches = re.finditer(temp_k, genome)
    matches_pos = [match.start() for match in matches]
    if len(matches_pos) >= t:
        for j in range(len(matches_pos) - 2):
            if matches_pos[j+2] - matches_pos[j] <= L - (k + 1):
                gen_niz.append(temp_k)
                break

rez = ''
for el in gen_niz:
    rez += el + ' '
    
print(rez)
