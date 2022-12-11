# 44:41

def get_lines():
    # file = open("input.txt", "r")
    file = open("example.txt", "r")
    lines = file.readlines()
    return lines

def main():
    lines = get_lines()
    count = 0
    for line in lines:
        line = line.strip()
        from_one = line[0]
        to_one = line[2]
        lis = line.split(',')
        first = lis[0].split('-')
        second = lis[1].split('-')
        print(first, second)
        
        # 2-8,3-7
        if first[0] <= second[0] and first[1] >= second[1]:
            
            print("one contains the other")
            count += 1
        elif first[0] >= second[0] and first[1] <= second[1]:
            print("One contaisn the other")
            count += 1
    print(count)
    
    
# Part 1
# two_comp_total()
# Part 2
main()


