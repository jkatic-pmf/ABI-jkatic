#BA1B

dna = input()
k = int(input())

d = dict()

for i in range(len(dna)):
    temp = dna[i:i+k]
    if temp in d: d[temp] += 1
    else: d[temp] = 1

max_val = max(d.values())

rez = [k for k, v in d.items() if v == max_val]
txt = ""
for el in rez:
    txt += el + " "
print(txt)
