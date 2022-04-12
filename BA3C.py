#BA3C

import sys

niz = [x.strip() for x in sys.stdin.readlines()]
k = len(niz[0])
while len(niz) > 1:
    prvi = niz.pop(0)
    for i in range(len(niz)):
        L = len(niz[i])
        if niz[i][:L-1] == prvi[-(L-1):]:
            el = prvi + niz[i][L-1:]
            niz.pop(i)
            niz.insert(0, el)
            break
        if prvi[:L-1] == niz[i][-(L-1):]:
            el = niz[i] + prvi[L-1:]
            niz.pop(i)
            niz.insert(0, el)
            break

dna = niz[0]
rez = ''
for i in range(len(dna)-k):
    rez += dna[i:i+k] + ' -> ' + dna[i+1:i+k+1] + '\n'

print(rez)
