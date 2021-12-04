filename = 'day4_input.txt'
input = open(filename).read()
lines = input.split('\n\n')
numbers = lines[0].split(',')
turns = 100

def check_win(board, numbers):
    for i in range(0, 21, 5):
        row = board[i:i+5]
        test_row = numbers[i: i+5]
        if row == test_row:
            return True
    for i in range(0, 5):
        column = [board[i], board[i+5], board[i+10], board[i+15], board[i+20]]
        test_column = [numbers[i], numbers[i+5], numbers[i+10], numbers[i+15], numbers[i+20]]
        if column == test_column:
            return True
    return False

def calculate_score(board, numbers, turns):
    unmarked = 0
    for i in range(0, len(board)):
        if board[i] == numbers[i]:
            continue
        else:
            unmarked = unmarked + int(board[i])
    score = unmarked * turns
    return score


for i in range(1, len(lines)):
    board_matrix = lines[i]
    board_str = board_matrix.replace('\n', ' ')
    test = [0] * 25
    board = board_str.split(' ')
    board = [i for i in board if i]
    for j in range(0, len(numbers)):
        for k in range(0, 25):
            if board[k] == numbers[j]:
                test[k] = numbers[j]
        bingo = check_win(board, test)
        if bingo == True and j < turns:
            turns = int(j)
            score = calculate_score(board, test, int(numbers[j]))
            break
print(score)



