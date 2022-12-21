# 28:21
def get_lines():
    # file = open("input.txt", "r")
    file = open("example.txt", "r")
    lines = file.readlines()
    return lines

def get_monkeys(lines):
    monkey_instr = []
    monkey_lis = []
    for line in lines:
        line = line.strip(" ")
        line = line.strip("\n")
        line = line.strip(",")
        monkey_instr.append(line.split(' '))                
        if line == '':
            print(monkey_instr)
            items = monkey_instr[1]
            operation = monkey_instr[2]
            first_action = operation[3]
            sign = operation[4]
            second_action = operation[5]
            tot_items = []
            for i in range(2, len(items)):
                print(i)
                item  = items[i].strip(',')
                tot_items.append(item)
           
            monkey = {
            "items" : tot_items,
            "operations" : [first_action,sign,second_action],
            }   
            monkey_lis.append(monkey)
            monkey_instr = []
    return monkey_lis

def main():
    lines = get_lines()    
    total_worry = 0
    monkeys = get_monkeys(lines)
    for monkey in monkeys:
        print(monkey)

    


# Part 1
# complete_overlap()
# Part 2
main()


