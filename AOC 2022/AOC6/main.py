file = open('input.txt', 'r')

characters = []

while 1:
    char = file.read(1)
    if not char:
        break
    characters.append(char)

while 1:
    for index in range(0, len(characters)):
        next_3 = [characters[index+1], characters[index+2], characters[index+3]]
        set_3 = set(next_3)
        if len(set_3) != len(next_3):
            pass
        else:
            if characters[index] not in next_3:
                print(index+4)
                break
print(characters)
    