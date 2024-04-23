file = open('test.txt', 'r')
lines = file.readlines()
for line in lines:
    values = line.Split(' ')