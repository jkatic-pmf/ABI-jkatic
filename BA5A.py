#BA5A

money = int(input())
change_in = input()
change_in = change_in.split(',')
change = []
for n in change_in:
    change.append(int(n))


min_change = (money + 1) * [0]

for i in range(1, money + 1):
    min_change[i] = i + 1
    for c in change:
        if i >= c and min_change[i - c] + 1 < min_change[i]:
            min_change[i] = min_change[i - c] + 1

print(min_change[-1])
