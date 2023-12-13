#Star 1 complete Star 2 incomplete 
###STAR 1
file = open('input.txt', 'r')
lines = file.readlines()

def star_one(lines):
    points = 0 
    for line in lines: 
        card, values = line.strip().split(':')
        print(card)
        winning, hand = values.strip().split('|')
        match_count = 0 
        winning_cards = winning.strip().split(" ")
        for value in winning_cards:
            if value.strip() in hand.strip().split(" "): 
                if value == '':
                    pass
                else: 
                    match_count = match_count+1 
                    print(value)
        print(match_count)
        points = int(points) + int(pow(2, match_count-1))
        # print(points)
    
    return points

# print(star_one(lines))

map_scratchcards = {}

def star_two(lines):
    for line in lines: 
        card, values = line.strip().split(':')
        name_card, num_card = card.strip().split()
        print(num_card)
        if int(num_card) not in map_scratchcards:
            print(f'num not in scratcardmap {num_card}')
            map_scratchcards[int(num_card)] = 1
        print(card)
        winning, hand = values.strip().split('|')
        match_count = 0 
        winning_cards = winning.strip().split(" ")
        for value in winning_cards:
            if value.strip() in hand.strip().split(" "): 
                if value == '':
                    pass
                else: 
                    match_count = match_count+1 
        print(match_count)
        for i in range(1, match_count + 1):
            map_scratchcards[int(num_card) + i] = map_scratchcards.get(int(num_card) + i, 1) + 1*map_scratchcards.get(int(num_card))
        print(map_scratchcards)
    #     for num in range(int(num_card)+1, int(num_card)+match_count+1):
    #         map_scratchcards[num] = map_scratchcards.get(num, 1) + map_scratchcards[num_card]
    #     # print(points)
    # print(map_scratchcards)
    return sum(map_scratchcards.values())

print(star_two(lines))

file.close()