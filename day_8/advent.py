# 28:21
def check_right_side(lines, lis ):
    for line in lines:
        line = line.strip('')
        line = line.strip('\n')
        for i in range(len(line)):              
            guard = False
            for l in range(i):
                print("Tree being checked ", i)
                print("Checking ", line[i] , "and ", line[l])
                
                if line[i] > line[l]:
                    guard = True
                    break
            if guard == True:
                lis.append(line[i])
                guard= False
    return lis
def check_edges(lines,lis):
    for line in lines:
        line = line.strip('')
        line = line.strip('\n')

def get_lines():
    # file = open("input.txt", "r")
    file = open("example.txt", "r")
    lines = file.readlines()
    return lines
def check_left_side(lines, lis ):
    lis = []
    for line in lines:
        line = line.strip('')
        line = line.strip('\n')
        for i in range(len(line)):              
            guard = True
            count = 0
            for l in range(i):
                if count == (l+1): 
                    if line[i] > line[l]:
                        count += 1
                else:
                    guard = False
            if guard:
                lis.append(line[i])
        
        print("Total ", lis)
                


                # rev = l - len(line) # 0 - 6 = -6
                # print("The rev index ", rev)
                # if line[i] > line[rev]:
                #     lis.append(line[i])
                #     break

    print("Total ", len(lis))
    return lis


                
def main():
    lines = get_lines()
    lis = []
    total = 0
    for line in lines:
        line_len = len(line)
        line = line.strip(" ")
        line = line.strip("\n")
        lis.append(line)
    y = 0
    for x in range(len(lis)):
        #Check first column
        totalBefore = total
        for y in range(len(lis[x])):
            # if x == 0 or x == (len(lis) -1):
                # total += 1
                # break
            # Check left, should be 11 cases in the test sample
            left_guard = True 
            right_guard = True
            up_guard = True
            down_guard = True
            for i in range(y):
                # Check from left, 11 cases
                if not (lis[x][y] > lis[x][i]):
                    left_guard = False
                rev = i - len(lis[x])
                # Check from right, 11 cases 
                if not (lis[x][y]) < lis[x][rev]:
                    right_guard = False
                # Check above
                up_guard = True
                down_guard = True
                if x == 0:
                    break
                # Where x is the lines of trees above
                for j in range(x):
                    # if tree being checked is not larger than line j with the same y index
                    if not (lis[x][y] > lis[j][y]):
                        up_guard = False
                # Check trees below
                for h in range(len(lis) - (x) ):
                    rev = h - x 
                    # print("x ", x , "Rev ",rev )
                    if x == 4 and y == 2:
                        print("Checking last row")
                        print(len(lis) - x  )
                        print("ALl guards")
                        print( left_guard , right_guard, up_guard, down_guard)
                    if x == len(lis):
                        pass

                    elif not (lis[x][y] > lis[rev][y]):
                        down_guard = False
                    


            if left_guard or right_guard or up_guard or down_guard: 
                total += 1
            left_guard = True
            right_guard = True
            up_guard = True 
            down_guard = True
            # Should be 21 cases in total for test
            
        print('Amount in ', x, "a:  ", total-totalBefore )
    

    print("total ", total)
        # Check above
                



        
    print(lis)
    # lis = check_right_side(lines, lis)
    # print(lis)
    # print(len(lis))

    


# Part 1
# complete_overlap()
# Part 2
main()


