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

def part_two(input):
    file = open(input, 'r')
    reports = file.readlines()
    unsafeReports = 0
    for report in reports:
        values = report.strip().split(" ")
        isSafe=True
        difs = []

        for index in range(0, len(values)-1):
            difs.append(int(values[index])-int(values[index+1]))

        direction = difs[0]
        unsafeLevels = 0
        for dif in difs: 
            if dif > 3 or dif < -3 or dif ==0:

                # isSafe = False
                unsafeLevels = unsafeLevels +1
                # print(f"difference too great: {dif}")
        
            elif direction > 0 and dif < 0:
                # print("inside positive dif wrong direction")
                # isSafe = False
                unsafeLevels = unsafeLevels +1
                # print(f"direction wrong: {direction}, dif: {dif}")
                
            elif direction < 0 and dif > 0:
                # print("inside positive dif wrong direction")
                # isSafe = False
                unsafeLevels = unsafeLevels +1
                # print(dif)
                # print(f"direction wrong: {direction}, dif: {dif}")
        print(f"unsafe levels: {unsafeLevels}")
        if unsafeLevels > 1:
            isSafe = False
        # print(f"isSafe: {isSafe}")    
        if isSafe == True:
            print(values)
        if isSafe == False: 
            unsafeReports = unsafeReports+1
    print(6-unsafeReports)    

part_two('test-input.txt')