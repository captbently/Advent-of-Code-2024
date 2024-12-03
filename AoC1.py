from collections import Counter

a, b = [], []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)

a.sort()
b.sort()
print(a)
print(b)

n = len(a)

# Part 1
print(sum(abs(a[i] - b[i]) for i in range((n))))

# Part 2
c = Counter(b)
print(sum(a[i]*c[a[i]] for i in range(n)))