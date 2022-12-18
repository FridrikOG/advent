# 52:08

def get_lines():
    file = open("input.txt", "r")
    # file = open("example.txt", "r")
    lines = file.readlines()
    return lines

def display_stacks(stacks):
    for stack in stacks:
        print(stack, stacks[stack])
def get_stack_len(lines):
    dic = {}|
    for line in lines:
        line = line.strip()
        if len(line) != 0:            
            if line[0] =='1':
                print("Found the line with crates ")
                # line = line.replace(" ", "")
                stack_len = int(line[-1])
                count = 0
                for i in line:
                    count += 1
                    if i.isdigit():
                        # Get the index for each stack
                        dic[i] = count
                return dic

def new_order():
    lines = get_lines()
    count = 0
    dic = get_stack_len(lines)
    stacks = {}
    for i in dic:
        stacks[i] = []

    for line in lines:
        if line[1] == '1':
            break
        for key in dic:
            # print(dic[key])
            index = dic[key]
            # print("index ", index)
            if len(line) > index:
                if line[index].strip(' ') != '':
                    stacks[key].append(line[index])
    # display_stacks(stacks)

    for line in lines:
        if line[0] == 'm':
            count += 1
            lis = line.strip('\n').split(' ')
            amount_to_move = int(lis[1])
            frm = lis[3]
            to = lis[5]
            for i in range(amount_to_move):
                print(stacks[frm][0])
                rmv = stacks[frm][0]
                stacks[frm] = stacks[frm][1:]
                stacks[to].insert(0,rmv)
                # stacks[to].append(stacks[frm].remove(1))
            display_stacks(stacks)
    strn = ""
    for i in stacks:
        strn += stacks[i][0]
    print(strn)
        
def maintain_order():
    lines = get_lines()
    count = 0
    dic = get_stack_len(lines)
    stacks = {}
    for i in dic:
        stacks[i] = []

    for line in lines:
        if line[1] == '1':
            break
        for key in dic:
            # print(dic[key])
            index = dic[key]
            # print("index ", index)
            if len(line) > index:
                if line[index].strip(' ') != '':
                    stacks[key].append(line[index])
    # display_stacks(stacks)

    for line in lines:
        if line[0] == 'm':
            count += 1
            lis = line.strip('\n').split(' ')
            amount_to_move = int(lis[1])
            frm = lis[3]
            to = lis[5]
            for i in range(amount_to_move):
                print(stacks[frm][0])
                rmv = stacks[frm][0]
                stacks[frm] = stacks[frm][1:]
                stacks[to].insert(i,rmv)
            display_stacks(stacks)
    strn = ""
    for i in stacks:
        strn += stacks[i][0]
    print(strn)
# Part 1
# new_order()
# Part 2
maintain_order()



