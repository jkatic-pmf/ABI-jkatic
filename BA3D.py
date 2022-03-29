#BA3D

from collections import defaultdict

k = int(input())
txt = input()

niz = []
for i in range(len(txt) - (k-1)):
    #d[txt[i:i+(k-1)]] = txt[i+1:i+k]
    niz.append((txt[i:i+(k-1)], txt[i+1:i+k]))

d = defaultdict(list)
for key, val in niz:
    d[key].append(val)

for k in d:
    val = ''
    for i in range(len(d[k])):
        val += d[k][i] + ','
    val = val[:-1]
    print(k + ' -> ' + val)
