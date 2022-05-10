#BA4C

mass = {
    "G": 57,
    "A": 71,
    "S": 87,
    "P": 97,
    "V": 99,
    "T": 101,
    "C": 103,
    "I": 113,
    "L": 113,
    "N": 114,
    "D": 115,
    "K": 128,
    "Q": 128,
    "E": 129,
    "M": 131,
    "H": 137,
    "F": 147,
    "R": 156,
    "Y": 163,
    "W": 186,
}

peptide = input()

niz = []
for el in peptide:
    niz.append(mass[el])

rez = []
p = niz.copy()
for i in range(len(niz)):
    for j in range(2, len(niz)):
        rez.append(sum(p[0:j]))
    #rez.append()
    p.append(p.pop(0))

for el in niz:
    rez.append(el)
rez.append(0)
rez.append(sum(niz))
rez.sort()

s = ''
for el in rez:
    s += str(el) + ' '

print(s)
