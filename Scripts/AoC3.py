import re

with open('Input Text/input3.txt') as f:
    multi = f.read().strip()
        
# Part 1
'''
matches = re.findall(r"mul\((\d+),(\d+)\)", multi)
print(matches)

matched = 0
for match in matches:
    matched += int(match[0]) * int(match[1])

print(matched)
'''

# Part 2
matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", multi)
print(matches)

enabled = 0

matched = 0
for match in matches:
    if match[2] == "" and enabled:
        matched += int(match[0]) * int(match[1])
    else:
        if match[2] == "do()":
            enabled = True
        else:
            enabled = False

print(matched)