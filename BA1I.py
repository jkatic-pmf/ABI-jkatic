#BA1I

import itertools

txt = input()
k = int(input())
d = int(input())
    
patterns = {}
num_patt = list(itertools.product(range(4), repeat=k))
val = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
for el in num_patt:
    k_el = ''
    for i in el:
        k_el += val[i]
    patterns[k_el] = 0

for el in patterns:
    for i in range(len(txt)-k+1):
        if el == txt[i:i+k]:
            patterns[el] += 1
        else:
            dif = 0
            el2 = txt[i:i+k]
            for j in range(k):
                if el[j] != el2[j]:
                    dif += 1
                    if dif > d:
                        break
            if dif <= d:
                patterns[el] += 1

max_val = max(patterns.items(), key=lambda x: x[1])[1]
val_l = []
for key, val in patterns.items():
    if val == max_val:
        val_l.append(key)

rez = ''
for el in val_l:
    rez += el + ' '
print(rez)
