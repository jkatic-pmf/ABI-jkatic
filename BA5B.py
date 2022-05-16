#BA5B

import sys

inlines = [x.strip('\n') for x in sys.stdin.readlines()]
n, m = [int(x) for x in inlines[0].split()]

down = []
for i in range(n):
    down.append([int(x) for x in inlines[1 + i].split()])

right = []
for i in range(n+1):
    right.append([int(x) for x in inlines[n + 2 + i].split()])


mat = []

for i in range(n + 1):
    mat.append((m + 1) * [0])

for i in range(1, m + 1):
    mat[0][i] = mat[0][i-1] + right[0][i-1]
for i in range(1, n + 1):
    mat[i][0] = mat[i-1][0] + down[i-1][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        mat[i][j] = max(mat[i-1][j] + down[i-1][j], mat[i][j-1] + right[i][j-1])

print(mat[n][m])
