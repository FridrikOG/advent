# 28:21

def get_lines():
    file = open("input.txt", "r")
    # file = open("example.txt", "r")
    lines = file.readlines()
    return lines


def check_range(range_one, range_two):
    start_one, end_one = map(int, range_one.split('-'))
    start_second, end_second = map(int, range_two.split('-'))
    print("Comarping ", start_one , end_one, start_second, end_second)
    return start_second <= start_one and end_one <= end_second
def complete_overlap():
    lines = get_lines()
    count = 0
    for line in lines:
        line = line.strip()
        lis = line.split(',')
        if check_range(lis[0], lis[1]) or check_range(lis[1], lis[0]):
            count += 1
    print(count)

def check_range_any(range_one, range_two):
    ''' Check if range one has any overlap with range two'''
    start_one, end_one = map(int, range_one.split('-'))
    start_second, end_second = map(int, range_two.split('-'))
    # 6-6,4-6
    return start_one <= end_second and end_one >= start_second 

def any_overlap():
    lines = get_lines()
    count = 0
    for line in lines:
        line = line.strip()
        lis = line.split(',')
        if check_range_any(lis[0], lis[1]) or check_range_any(lis[1], lis[0]):
            count += 1
    print(count)
    
# Part 1
# complete_overlap()
# Part 2
any_overlap()



