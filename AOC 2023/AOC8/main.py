file = open('input.txt', 'r')
lines = file.readlines()

pattern = ""

# print(lines)
count = 0
while lines[count] != '\n':
    pattern = pattern + lines[count].strip()
    count = count + 1 
    
mapping_dict = {}
for i in range(count+1, len(lines)):
    letter, code = lines[i].strip().split('=')
    letter = letter.strip()
    left, right = code.strip(' ( ) ').split(',')
    left = left.strip()
    right = right.strip()
    mapping_dict[letter] = {'L': left, 'R': right}

print(mapping_dict)

value = 'AAA'
count = 0
while value != 'ZZZ':
    for code in pattern: 
        count = count + 1 
        value = mapping_dict[value][code]
print(count)


print(pattern)

