


def get_lines():
    file = open("input.txt", "r")
    lines = file.readlines()
    return lines

def top_cal_elf():
    lines = get_lines()
    max_cal = 0
    current = 0
    for line in lines:
        print(line, len(line.strip()))
        line = line.strip()
        if len(line) == 0:
            current = 0
        else:
            line = int(line)
            current += line
            if current > max_cal:
                max_cal = current
        
    print("Max cal is: ", max_cal)
        
def top_three_cal_combined():
    lines = get_lines()
    max_list = [0,0,0]
    current = 0
    for line in lines:
        print(line, len(line.strip()))
        line = line.strip()
        if len(line) == 0:
            current = 0
        else:
            line = int(line)
            current += line
            if current > max_list[0]:
                max_list[0] = current
        max_list = sorted(max_list)
    print(sum(max_list))
    # print("Max cal is: ", max_cal)
    
    
top_three_cal_combined()