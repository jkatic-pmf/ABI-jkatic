#BA1H

pattern = input()
text = input()
d = int(input())

pozicije = ""

for i in range(len(text)-len(pattern)):
     br = 0
     text_part = text[i:len(pattern)+i]
     for j in range(len(pattern)):
          if text_part[j] != pattern[j]:
               br += 1
     if br <= d:
          pozicije += str(i) + " "

print(pozicije)
