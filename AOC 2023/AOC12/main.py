file = open('test.txt', 'r')
lines = file.readlines()
count = 0
for line in lines: 
    sequence, pattern = line.strip().split(' ')
    sequence = list(sequence)
    sum_units = 0
    list_pattern = []
    for value in pattern.split(','):
        list_pattern.append(value)
        sum_units = int(value) + sum_units + 1
    if (sum_units-1) == len(sequence):
        count = count + 1
    else: 
        print(sequence)
        for v in sequence:
            if v == '?':
                count = count + 1
        print(count)
print(len(lines))
print(count)
