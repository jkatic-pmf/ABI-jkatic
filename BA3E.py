#BA3E

from collections import defaultdict
import sys
niz = [x.strip() for x in sys.stdin.readlines()]

n = []
for i in range(len(niz)):
    n.append((niz[i][:-1], niz[i][1:]))

d = defaultdict(list)
for key, val in n:
    d[key].append(val)

for k in d:
    val = ''
    for i in range(len(d[k])):
        val += d[k][i] + ','
    val = val[:-1]
    print(k + ' -> ' + val)
