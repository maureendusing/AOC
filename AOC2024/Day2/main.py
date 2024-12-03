def part_one(input):
    file = open(input, 'r')
    reports = file.readlines()
    unsafeReports = 0
    for report in reports:
        values = report.strip().split(" ")
        #print(f"values:{values}")
        isSafe=True
        difs = []

        for index in range(0, len(values)-1):
            difs.append(int(values[index])-int(values[index+1]))

        direction = difs[0]
        # if direction == 0:
        #     print("YOU IDIOT")
        #     print(f"values:{values}")
            
        #print(f"direction: {difs[0]}")
        for dif in difs: 
            if dif > 3 or dif < -3 or dif ==0:
                isSafe = False
                
                # print(f"difference too great: {dif}")
        
            if direction > 0 and dif < 0:
                # print("inside positive dif wrong direction")
                isSafe = False
                # print(f"direction wrong: {direction}, dif: {dif}")
                
            if direction < 0 and dif > 0:
                # print("inside positive dif wrong direction")
                isSafe = False
                # print(dif)
                # print(f"direction wrong: {direction}, dif: {dif}")
                    
                # elif direction == 0:
                    # print("YOU IDIOT")
                    # print(f"values:{values}")
        # print(f"isSafe: {isSafe}")    
        if isSafe == True:
            print(values)
        if isSafe == False: 
            unsafeReports = unsafeReports+1
    print(1000-unsafeReports)

def check_safe(values):
    isSafe=True
    difs = []

    for index in range(0, len(values)-1):
        difs.append(int(values[index])-int(values[index+1]))

    direction = difs[0]

    for dif in difs:
        if dif > 3 or dif < -3 or dif ==0:
            isSafe = False
        if direction > 0 and dif < 0:
            isSafe = False
        if direction < 0 and dif > 0:
            isSafe = False
    return isSafe

def part_two(input):
    file = open(input, 'r')
    reports = file.readlines()
    safeReports = 0
    for report in reports:
        values = report.strip().split(" ")
        # print(values)
        #print(f"values:{values}")
        isSafe=True
        difs = []
        if check_safe(values):
            safeReports =safeReports + 1
        else: 
            for index in range(0,len(values)-1):
                new_list = values
                new_list[0:index:1]
                print(new_list)
                if check_safe(new_list):
                    safeReports = safeReports + 1
                    continue


       
    print(safeReports)

part_two('test-input.txt')