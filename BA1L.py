# BA1L

# A = 0
# C = 1
# G = 2
# T = 3

val = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def PattToNum(patt):
    if len(patt) == 0:
        return 0

    el = patt[-1]
    num = val[el]
    prefix = patt[:-1]
    return 4 * PattToNum(prefix) + num

patt = input()
rez = PattToNum(patt)
print(rez)
