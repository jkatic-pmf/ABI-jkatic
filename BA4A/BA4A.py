#BA4A

import ast

with open('data.txt') as f:
    data = f.read()

d = ast.literal_eval(data)

rna = input()
amino_acid = ''

for i in range(0, len(rna)-2, 3):
    amino_acid += d[rna[i:i+3]]

print(amino_acid[:-1])
