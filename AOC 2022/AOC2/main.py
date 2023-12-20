file = open('input.txt', 'r')
lines = file.readlines()
 
def star_one(lines):
    opponent = {'A': 1, 'B': 2, 'C': 3}
    you = {'X': 1, 'Y': 2, 'Z': 3}
    score = 0 
    for line in lines:
        opp, u = line.strip().split(' ')
        if you[u] == opponent[opp]:
            score = score + 3 + you[u]
        elif you[u] == 1: #rock
            if opponent[opp] == 3: #Scissors
                score = score + 6 + you[u]
            if opponent[opp] == 2: #paper 
                score = score + you[u]
        elif you[u] == 2: #Paper 
            if opponent[opp] == 1: #Rock 
                score = score + 6 + you[u]
            if opponent[opp] == 3: #Scissors 
                score = score + you[u]
        elif you[u] == 3: #Scissors
            if opponent[opp] == 1: #Rock
                score = score + you[u]
            if opponent[opp] == 2: #Paper
                score = score + 6 + you[u]
    print(score)

star_one(lines)

def star_two(lines):
    you = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    opponent = {'A': 1, 'B': 2, 'C': 3}
    score = 0 
    for line in lines:
        opp, u = line.strip().split(' ')
        if u == 'Y': #tie
            score = score + 3 + opponent[opp]
        elif u == 'X': #lose
            if opponent[opp] == 3: #Scissors
                score = score + 2 
            if opponent[opp] == 2: #paper 
                score = score + 1
            if opponent[opp] == 1: #Rock
                score = score + 3
        elif u == 'Z': #win 
            if opponent[opp] == 1: #Rock 
                score = score + 6 + 2
            if opponent[opp] == 3: #Scissors 
                score = score + 6 + 1
            if opponent[opp] == 2:
                score = score + 6 + 3
    print(score)

star_two(lines)