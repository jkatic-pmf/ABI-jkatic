#BA1N

import itertools

def test(k, dna, d):
    br = 0
    for i in range(len(k)):
        if k[i] != dna[i]: br += 1
        if br > d: return False
    return True

dna = input()
d = int(input())

m = ['A', 'C', 'G', 'T']

patterns = []
num_patt = list(itertools.product(range(4), repeat=len(dna)))
val = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
for el in num_patt:
    k_el = ''
    for i in el:
        k_el += val[i]
    if test(k_el, dna, d):
        patterns.append(k_el)

for el in patterns:
    print(el)
