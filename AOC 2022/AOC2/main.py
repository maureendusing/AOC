file = open('input.txt', 'r')
lines = file.readlines()

opponent = {'A': 1, 'B': 2, 'C': 3}
you = {'X': 1, 'Y': 2, 'Z': 3}

score = 0 
for line in lines:
    opp, u = line.strip().split(' ')
    if opponent[opp] < you[u]:
        score = score + 6 + you[u]
    else:
        if opponent[opp] == you[u]:
            score = score + 3 + you[u]
        else:
            score = score + you[u]
print(len(lines))
print(score)


