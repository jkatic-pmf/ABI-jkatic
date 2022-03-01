#BA1A

txt = input()
pat = input()

d = len(pat)

br = 0

for i in range(len(txt) - d + 1):
    if txt[i:i+d] == pat: br += 1

print(br)
