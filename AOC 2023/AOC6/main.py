###STAR 1 

# file = open('input.txt', 'r')
# lines = file.readlines()

# map_races = {}

def winning_options(race_time, best_dist):
    winning_options = 0
    for sec in range(1, int(race_time)):
        if(((int(race_time)-int(sec))*int(sec)) > int(best_dist)):
            winning_options = winning_options + 1 

    return winning_options
    
# def star_one():
#     i, race_distances = lines[0].strip().split(':')
#     j, race_best = lines[1].strip().split(':')
#     race_distances = race_distances.strip().split(' ')
#     race_best = race_best.strip().split('   ')
#     print(race_best)
#     count = 0
   
#     for race in race_distances: 
#         # print(race)
#         if race != '' and race_best[count] != '':
#             print(race, race_best[count])
#             map_races[race] = winning_options(race, race_best[count])
#             count = count + 1
#         else: 
#             print(race)
    
#     print(map_races)

#     total = 1
#     for key in map_races:
#         total = total*map_races[key]

#     return total


# print(star_one())

import time
start_time = time.time()
###STAR 2
    
def star_two():
    file = open('input.txt', 'r')
    lines = file.readlines()

    i, race_distances = lines[0].strip().split(':')
    j, race_best = lines[1].strip().split(':')
    race_distances = race_distances.strip()
    actual_distance = 0
    for dist in race_distances: 
        actual_distance = str(actual_distance) + str(dist.strip())
    actual_best = 0
    for best in race_best:
        actual_best = str(actual_best) + str(best.strip())
    print(actual_distance)
    print(actual_best)
    count = 0
   
    return winning_options(actual_distance, actual_best)


print(star_two())
print("Process finished --- %s seconds ---" % (time.time() - start_time))