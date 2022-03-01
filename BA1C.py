#BA1C

dna = input()
rez = ""

for el in dna:
    if el == 'A': rez += 'T'
    elif el == 'T': rez += 'A'
    elif el == 'C': rez += 'G'
    else: rez += 'C'

rev = reversed(rez)
print("".join(rev))
