
def get_lines():
    file = open("input.txt", "r")
    # file = open("example.txt", "r")
    lines = [row.strip() for row in file.readlines()]
    return lines
                
def main():
    lines = get_lines()
    cycle = 0
    x = 1
    check_cycle = 20
    the_sum = 0
    times_add = 0
    times_cycle_hit = 0
    for line in lines:
        instr = line.split(' ')
        if instr[0] ==  'noop':
            cycle_through = 1
        else:
            cycle_through = 2
        for i in range(1,cycle_through+1):
            if check_cycle == cycle:
                times_cycle_hit += 1
                the_sum = the_sum +  (x * check_cycle )
                print("Adding ", x * check_cycle)
                check_cycle += 40
                
            if i == 1:
                cycle += 1
            elif i == 2:
                x += int(instr[1])
                times_add += 1
                cycle +=1
            
            

    print(times_add)       
    print(the_sum)
    print(times_cycle_hit)

main()



