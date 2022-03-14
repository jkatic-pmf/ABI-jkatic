#BA2A

import itertools

k = int(input())
d = int(input())
dna = input()

niz = dna.split(' ')

patterns = []
num_patt = list(itertools.product(range(4), repeat=k)) # sve moguce varijacije (napravljeno s brojevima)
val = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
for el in num_patt:
    k_el = ''
    for i in el:
        k_el += val[i]
    patterns.append(k_el)

rez = []
for el in patterns:
    test = 0
    for n in niz:
        for i in range(len(n)-k+1):
            br = 0 #razlika
            for j in range(k):
                if el[j] != n[i+j]: br += 1
            if br <= d:
                test += 1
                break
    if test == len(niz):
        rez.append(el)

print(rez)
