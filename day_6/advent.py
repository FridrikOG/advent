# 14:41
        
def get_lines():
    file = open("input.txt", "r")
    # file = open("example.txt", "r")
    lines = file.readlines()
    return lines
        
def check_for_signal(amount_check = 4):
    lines = get_lines()
    count = 0
    line = lines[0]
    # print(line)
    str_lis = []
    print(set(str_lis))
    for i,x in enumerate(line):
        str_lis.append(x)
        index = len(str_lis)-amount_check 
        four_recent = str_lis[index:]
        if len(four_recent) == amount_check:
            print(set(four_recent), print(len(set(four_recent))))
            if len(set(four_recent)) == amount_check:
                print("found at index ",i +1)
                return
    print("Found none")
        
# Part 1
# check_for_signal()
# Part 2
check_for_signal(amount_check = 14)


