counter = [0 for i in range(10)]
number = input()

for i in number:
    counter[int(i)] += 1

if (counter[6] + counter[9]) % 2 == 1:
    val = (counter[6] + counter[9]) //2 +1
    counter[6] = val
    counter[9] = val
else:
    val = (counter[6] + counter[9]) //2
    counter[6] = val
    counter[9] = val

print(max(counter))

