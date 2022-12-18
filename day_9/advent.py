# 28:21
def get_lines():
    # file = open("input.txt", "r")
    file = open("example.txt", "r")
    lines = file.readlines()
    return lines
                
def main():
    lines = get_lines()
    lis = []
    for line in lines:
        line_len = len(line)
        line = line.strip(" ")
        line = line.strip("\n")
        lis.append(line)
                



        
    print(lis)
    # lis = check_right_side(lines, lis)
    # print(lis)
    # print(len(lis))

    


# Part 1
# complete_overlap()
# Part 2
main()


