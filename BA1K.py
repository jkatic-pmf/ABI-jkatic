#BA1K

import itertools

dna = input()
k = int(input())

patterns = {}
num_patt = list(itertools.product(range(4), repeat=k))
val = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
for el in num_patt:
    k_el = ''
    for i in el:
        k_el += val[i]
    patterns[k_el] = 0

for i in range(len(dna) - k+1):
    patterns[dna[i:i+k]] += 1

rez = list(patterns.values())
rez_str = ''
for el in rez:
    rez_str += str(el) + ' '
print(rez_str)
