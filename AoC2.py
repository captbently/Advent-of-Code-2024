reports = []

with open('input2.txt', 'r') as f:
    for line in f.readlines():
        reports.append([int(z) for z in line.split()])

# Part 1
def is_safe(l):
    n = len(l)
    return (all(1 <= l[i+1]-l[i] <= 3 for i in range(n-1))) or (all(1 <= l[i]-l[i+1] <= 3 for i in range(n-1)))

count = sum(map(is_safe, reports))
print(count)

# Part 2
count2 = 0
for report in reports:
    count2 += (is_safe(report) or any(is_safe(report[:i] + report[i+1:]) for i in range(len(report))))

print(count2)