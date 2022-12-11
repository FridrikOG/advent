# 44:41

def get_lines():
    file = open("input.txt", "r")
    # file = open("example.txt", "r")
    lines = file.readlines()
    return lines

def two_comp_total():
    lines = get_lines()
    lower_val = 96
    upper_val = 38
    score = 0
    for line in lines:
        line = line.strip()
        line_len = len(line)
        half_index = int((line_len/2))
        comp_one = line[0:half_index]    
        comp_two = line[half_index:]
        dups = set(comp_one) & set(comp_two)
        for dup in dups:
            if dup == dup.upper():
                print(dup, (ord(dup) - upper_val))
                score += (ord(dup) - upper_val)
            else:
                print(dup, (ord(dup) - lower_val))
                score +=  (ord(dup) - lower_val)
                
    print(score)

def three_group_total():
    lines = get_lines()
    lower_val = 96
    upper_val = 38
    score = 0
    count = 0
    dups = {}
    set_two = ''
    old_line = ''
    for line in lines:
        count += 1
        line = line.strip()
        if count == 2:
            set_two = set(line) & set(old_line)
            old_line = line    
        elif count == 3:
            set_two = set(set_two) & set(line)
            print("SEt two " ,set_two)
            for dup in set_two:
                if dup == dup.upper():
                    print(dup, (ord(dup) - upper_val))
                    score += (ord(dup) - upper_val)
                else:
                    print(dup, (ord(dup) - lower_val))
                    score +=  (ord(dup) - lower_val)
        old_line = line 
        if count >= 3:
                count = 0        
                dups = {}
                old_line = ''
                set_two = {}
    print(score)
    
        
# Part 1
# two_comp_total()
# Part 2
three_group_total()


