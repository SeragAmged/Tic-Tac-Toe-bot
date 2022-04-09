board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = 'O'
bot = 'X'
player2 = 'X'


def print_board(boarda):
    print(boarda[1] + '|' + boarda[2] + '|' + boarda[3])
    print('-+-+-')
    print(boarda[4] + '|' + boarda[5] + '|' + boarda[6])
    print('-+-+-')
    print(boarda[7] + '|' + boarda[8] + '|' + boarda[9])
    print("\n")


def space_is_free(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insert_letter(letter, position):
    if space_is_free(position):
        board[position] = letter
        print_board(board)
        if check_draw():
            print("Tie!")
            exit()
        if check_for_win(board):
            if letter == 'X' and x == 1:
                print("Computer wins!")
                exit()
            elif letter == 'X' and x == 2:
                print("X wins ")
                exit()
            elif letter == 'O' and x == 2:
                print("O wins ")
                exit()
            else:
                print("player wins")
    else:
        print("This position is already occupied!")
        position = int(input("Please enter new position:  "))
        insert_letter(letter, position)
        return


def check_for_win(boarda):
    if boarda[1] == boarda[2] and boarda[1] == boarda[3] and boarda[1] != ' ':
        return True
    elif boarda[4] == boarda[5] and boarda[4] == boarda[6] and boarda[4] != ' ':
        return True
    elif boarda[7] == boarda[8] and boarda[7] == boarda[9] and boarda[7] != ' ':
        return True
    elif boarda[1] == boarda[4] and boarda[1] == boarda[7] and boarda[1] != ' ':
        return True
    elif boarda[2] == boarda[5] and boarda[2] == boarda[8] and boarda[2] != ' ':
        return True
    elif boarda[3] == boarda[6] and boarda[3] == boarda[9] and boarda[3] != ' ':
        return True
    elif boarda[1] == boarda[5] and boarda[1] == boarda[9] and boarda[1] != ' ':
        return True
    elif boarda[7] == boarda[5] and boarda[7] == boarda[3] and boarda[7] != ' ':
        return True
    else:
        return False


def check_which_mark_won(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False


def check_draw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def player_move():
    run = True
    while run:
        position = input("Enter the position for 'O':  ")
        try:
            position = int(position)
            if 0 < position < 10:
                insert_letter(player, position)
                run = False
            else:
                print('Please type a number within the range!')
        except ValueError:
            print('Please type a number!')

    return


def player2_move():
    run = True
    while run:
        position = input("Enter the position for 'x':  ")
        try:
            position = int(position)
            if 0 < position < 10:
                insert_letter(player2, position)
                run = False
            else:
                print('Please type a number within the range!')
        except ValueError:
            print('Please type a number!')

    return


def comp_move():
    best_score = -800
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key

    insert_letter(bot, best_move)
    return


def minimax(boarda, depth, is_maximizing):
    if check_which_mark_won(bot):
        return 2
    elif check_which_mark_won(player):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -800
        for key in boarda.keys():
            if boarda[key] == ' ':
                boarda[key] = bot
                score = minimax(boarda, depth - 1, False)
                boarda[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in boarda.keys():
            if boarda[key] == ' ':
                boarda[key] = player
                score = minimax(boarda, depth - 1, True)
                boarda[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


print("Positions are as follow:")
print("1|2|3")
print('-+-+-')
print("4|5|6")
print('-+-+-')
print("7|8|9")
print("\n")


def player_goes_first():
    while not check_for_win(board):
        player_move()
        comp_move()


def player_goes_second():
    while not check_for_win(board):
        comp_move()
        player_move()


while True:
    answer = input('Do you want to play ? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        print('-----------------------------------')

        x = int(input("Do you want to play: \n "
                      "1. PLayer vs AI\n "
                      "2. player vs player "))
        if x == 1:
            answer2 = input("Do you want to play first?  (Y/N)")
            if answer2.lower() == 'y' or answer2.lower == 'yes':
                player_goes_first()
            else:
                player_goes_second()
        elif x == 2:
            while not check_for_win(board):
                player_move()
                player2_move()
    else:
        break
