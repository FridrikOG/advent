
# 1 for rock
# 2 for paper 
# 3 for scissors
# 0 loss
# 3 draw
# 6 win

# Rock = A X
# Paper = B Y
# Scissors = C Z


def get_lines():
    file = open("input.txt", "r")
    lines = file.readlines()
    return lines

def check_win(op_move, our_move):
    # draw
    if op_move == 'A' and  our_move == 'X' or op_move == 'B' and our_move == 'Y' or op_move == 'C' and our_move == 'Z':
        return 'draw'
    # win
    elif op_move == 'A' and our_move == 'Y' or op_move == 'B' and our_move == 'Z' or op_move == 'C' and our_move == 'X':
        return 'win'
    # loss
    elif op_move == 'A' and our_move == 'Z' or op_move == 'B' and our_move == 'X' or op_move == 'C' and our_move == 'Y':
        return 'loss'

def score_winner():
    lines = get_lines()
    score = 0
    for line in lines:
        op_move = line[0]
        our_move = line[2]
        print(op_move, our_move)
        print(line, len(line))
        result = check_win(op_move, our_move)
        if line[2] == 'X':
            score += 1
        elif line[2] == 'Y':
            score += 2
        elif line[2] == 'Z':
            score += 3
        if result == 'win':
            score += 6
        elif result == 'draw':
            score += 3
        elif result == 'loss':
            score += 0
    print("Answer to part 1 " , score)
            

def decided_winner():
    lines = get_lines()
    score = 0
    for line in lines:
        op_move = line[0]
        our_instr = line[2]
        if our_instr =='X':
            # We need to lose
            if op_move == 'A':
                our_move = 'Z'
            elif op_move == 'B':
                our_move = 'X'
            elif op_move == 'C':
                our_move = 'Y'
        if our_instr == 'Y':
            # draw
            if op_move == 'A':
                our_move = 'X'
            elif op_move == 'B':
                our_move = 'Y'
            elif op_move == 'C':
                our_move = 'Z'
        if our_instr == 'Z':
            # we need to win
            if op_move == 'A':
                our_move = 'Y'
            elif op_move == 'B':
                our_move = 'Z'
            elif op_move == 'C':
                our_move = 'X'

        result = check_win(op_move, our_move)
        if our_move == 'X':
            score += 1
        elif our_move == 'Y':
            score += 2
        elif our_move == 'Z':
            score += 3
        if result == 'win':
            score += 6
        elif result == 'draw':
            score += 3
        elif result == 'loss':
            score += 0
    print("Answer to part 2 " , score)
        
# Part 1
# score_winner()
# Part 2
decided_winner()