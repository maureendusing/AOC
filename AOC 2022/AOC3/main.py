file = open('test.txt', 'r')
lines = file.readlines()

charstr='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
def star_one(lines):
    for line in lines:
        half = int(len(line.strip())/2)
        compartment1 = line[0:half]
        compartment2 = line[half:]
        for value in compartment1:
            if value in compartment2:
                both = value
        total = total + (charstr.index(both) + 1)
    return total