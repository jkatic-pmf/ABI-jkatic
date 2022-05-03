#BA4B

import ast

with open('data.txt') as f:
    data = f.read()

d = ast.literal_eval(data)

dna = input()
acid = input()

dna_u = ''
for i in range(len(dna)):
    if dna[i] == 'T':
        dna_u += 'U'
    else:
        dna_u += dna[i]

rez = ''
rev_d = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
for i in range(len(dna_u)-(len(acid)*3-1)):
    amino_acid = ''
    rev_amino_acid = ''
    sample = dna_u[i:i+len(acid)*3]
    rev_sample = ''
    for j in range(len(sample)):
        rev_sample = rev_d[sample[j]] + rev_sample
    for j in range(0, len(acid)*3-2, 3):
        amino_acid += d[sample[j:j+3]]
        rev_amino_acid += d[rev_sample[j:j+3]]
    if amino_acid == acid or rev_amino_acid == acid:
        rez += dna[i:i+len(acid)*3] + '\n'

print(rez)
