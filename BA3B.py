#BA3B

import sys
niz = [x.strip() for x in sys.stdin.readlines()]
k = len(niz[0])

txt = niz[0]
for i in range(1, len(niz)):
    txt += niz[i][-1]
print(txt)
