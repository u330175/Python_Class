# bubble sort

import random

v = []
for i in range(1, 11):
    v.append(random.randint(1, 100))

print(v)

for i in range(1, 10):
    for j in range(0, 10-i):
        if (v[j] > v[j +1]):
            v[j], v[j+1] = v[j+1], v[j]

print(v)