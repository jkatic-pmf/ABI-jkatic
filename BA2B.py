#BA2B

import itertools

k = int(input())
dna = input()

niz = dna.split(' ')

patterns = []
num_patt = list(itertools.product(range(4), repeat=k))
val = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
for el in num_patt:
    k_el = ''
    for i in el:
        k_el += val[i]
    patterns.append(k_el)

min_distance = k*len(niz) + 1
k_mer = ''
for el in patterns:
    brojac = 0 #min_distance
    for n in niz:
        distance = k+1
        for i in range(len(n)-k+1):
            br = 0
            for j in range(k):
                if el[j] != n[i+j]: br += 1
            if br == 0:
                distance = br
                break
            elif br < distance:
                distance = br
        brojac += distance
    if brojac < min_distance:
        min_distance = brojac
        k_mer = el

print(k_mer)
            
