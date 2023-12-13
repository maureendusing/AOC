#Day 1 completed 
### first star
# import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()

total = 0
for line in lines: 
    digits = []
    for char in line: 
        if char.isnumeric():
            digits.append(char)
    print(len(digits))
    if len(digits) >= 2:
        number = digits[0] + digits[len(digits)-1]
    if len(digits) == 1:
        number = digits[0] + digits[0]
    
    # print(number)
    total = total + int(number)
print(total)


#second star work 
import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()
number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0
output_file = open('output.txt', 'w')
for line in lines: 
    digits = []
    for i,c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    score = int(digits[0]+digits[-1])
    total += score
print(total)
output_file.close()


