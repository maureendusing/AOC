import re

def part_one(input):
    file = open(input, 'r')
    corrupted_file = str(file.readlines())
    
    total = 0
    #find() method python: https://www.geeksforgeeks.org/python-string-find/
    #Step 1: find occuraces of instructionslike mul(X,Y) where X and Y are 1 to 3 digit numbers
    #Step 2: ignore if not accurate 
    #Step 3: multiply numbers together 
    search_pattern= r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(search_pattern,corrupted_file)
    for match in matches: 
        x = int(match[0])
        y = int(match[1])
        total = total + x*y
        print(f"X = {match[0]}, Y = {match[1]}")
    
    print(total)

# part_one("input.txt")

def part_two(input):
    
    file = open(input, 'r')
    corrupted_file = str(file.readlines())
    
    total = 0

    search_patterns= [r'mul\((\d{1,3}),(\d{1,3})\)', r'do\(\)', r"don\'t\(\)"]
    last_special_match = "do()"
    matches = []
    for pattern in search_patterns:
        for match in re.finditer(pattern, corrupted_file):
            matches.append({match.start(): match.group()})
            print(f"{match.group()}, {match.start()}")
            
    matches = sorted(matches, key=lambda d: next(iter(d)))
    print(matches)

    last_special_match = "do()"
    for match in matches:
        for key in match: 
            print(match)
            value = match[key]
            if value == "do()" or value == "don't()":
                last_special_match = value
            else:
                if last_special_match == "do()":
                    print(value)
                    x, y = value.split(',')
                    _, x = x.split('(')
                    y, _ = y.split(')')
                    x=int(x)
                    y=int(y)
                    total = total + x*y
            
    
    print(total)
part_two("input.txt")