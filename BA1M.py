#BA1M

# A = 0
# C = 1
# G = 2
# T = 3

val = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

def NumToPatt(num, k):
    if k == 1: return val[num]
    
    prefIndex = num//4
    ostatak = num%4
    patt = NumToPatt(prefIndex, k-1)
    return patt + val[ostatak]

num = int(input())
k = int(input())

rez = NumToPatt(num, k)
print(rez)
