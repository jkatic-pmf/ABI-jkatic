#BA3A

k = int(input())
txt = input()

rez = []
for i in range(len(txt)-k+1):
    rez.append(txt[i:i+k])

for el in rez:
    print(el)
