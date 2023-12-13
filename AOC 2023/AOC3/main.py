###NOT COMPLETED
import numpy
import csv

file = open('test.txt', 'r')
lines = file.readlines()

for line in lines: 
    for value in line: 
        # print(value)
        if value.isdigit():
            print(value)
print(lines)



    