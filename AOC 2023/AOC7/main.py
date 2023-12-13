file = open('test.txt', 'r')
lines = file.readlines()

letter_map = {'T': 'A', 'Q': 'B', 'K': 'C', 'A':'D', 'J': 'E'}

def determine_type(cards):
    counts = [cards.count(card) for card in cards]
    
    #first value in type determines what is the highest strength aka 7,6,5,4,3,2,1
    if 5 in counts: 
        return 6 
    if 4 in counts: 
        return 5 
    if 3 in counts: 
        if 2 in counts: 
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1 
    return 0

def strength(cards):
    return(determine_type(cards), [letter_map.get(card, card) for card in cards])

def sort_list(lines):
    plays = []
    for line in open('test.txt', 'r'): 
        cards, bet = line.strip().split(' ')
        plays.append((cards,int(bet)))
    plays.sort(key = lambda play: strength(play[0]))

    print(plays)
    
    winnings = 0
    for rank, (cards, bet) in enumerate(plays, 1):
        winnings = rank*bet + winnings
    return winnings
    #     cards = cards.strip()
    #     bet = bet.strip()
    #     sorted_list.append(cards)
    #     # print(sorted_list)
    # count = 0
    # for index in sorted_list: 
    #     if int(determine_type(index)) > int(determine_type(sorted_list[count+1])):
    #         temp = sorted_list[count]
    #         sorted_list[count] = sorted_list[count + 1]
    #         sorted_list[count + 1] = temp                                    
    #         #if the index > index + 1, swap places
    # print(sort_list)
    # return sorted_list

print(sort_list(lines))


