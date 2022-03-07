#BA1D

uzorak = input()
genome = input()

L = len(uzorak)
indexi = ""
for i in range(len(genome)):
     if genome[i:i+L] == uzorak:
          indexi += str(i) + " "

print(indexi)
