#BA3H

import sys

k = int(input())
niz = [x.strip() for x in sys.stdin.readlines()]

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

print(niz[0])
