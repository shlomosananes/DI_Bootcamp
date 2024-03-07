line1 = ['T', 'I', 'C', ' ', 'T', 'A', 'C', ' ', 'T', 'O', 'E', ' ', ' ', ' ', ' ', ' ', ' ']
line2 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
line3 = ['*', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '*']
line4 = ['*', ' ', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', '*']
line5 = ['*', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '*']
line6 = ['*', ' ', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', '*']
line7 = ['*', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '*']
line8 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

remaining_positions = {
    1: "Top Left",
    2: "Top Center",
    3: "Top Right",
    4: "Middle Left",
    5: "Middle Center",
    6: "Middle Right",
    7: "Bottom Left",
    8: "Bottom Center",
    9: "Bottom Right",
}

players = ('O', 'X')
current_player = 1
player = players[current_player]

moves_realized = 0
move = 1

end = 0


def display_board():
    print("".join(line1))
    print("".join(line2))
    print("".join(line3))
    print("".join(line4))
    print("".join(line5))
    print("".join(line6))
    print("".join(line7))
    print("".join(line8))


### Function to check if there is a win
def check_win():
    global player
    global end
    if (line3[4] == line3[8] == line3[12] == player or
        line5[4] == line5[8] == line5[12] == player or
        line7[4] == line7[8] == line7[12] == player or
        line3[4] == line5[4] == line7[4] == player or
        line3[8] == line5[8] == line7[8] == player or
        line3[12] == line5[12] == line7[12] == player or
        line3[4] == line5[8] == line7[12] == player or
        line7[4] == line5[8] == line3[12] == player):
        print(f"Congrats player {player}! You won!")
        end = 1


def switch_player():
    global current_player
    global player
    if current_player == 0:
        current_player = 1
    elif current_player == 1:
        current_player = 0
    player = players[current_player]
    print(f"Now it is player {player} turn.")


def player_input():
    global move
    move = int(input(f"Please pick your next move from the remaining positions: \n{remaining_positions}"))


# Function to update lines according to player's move
def update_lines():
    global move
    if move == 1:
        line3[4] = players[current_player]
    elif move == 2:
        line3[8] = players[current_player]
    elif move == 3:
        line3[12] = players[current_player]
    elif move == 4:
        line5[4] = players[current_player]
    elif move == 5:
        line5[8] = players[current_player]
    elif move == 6:
        line5[12] = players[current_player]
    elif move == 7:
        line7[4] = players[current_player]
    elif move == 8:
        line7[8] = players[current_player]
    elif move == 9:
        line7[12] = players[current_player]
    del remaining_positions[move]


def moves_count():
    global moves_realized
    moves_realized += 1


def play():
    global end
    global moves_realized
    while end == 0:
        if moves_realized == 9:
            print("The game ended on a tie!")
        elif moves_realized == 0:
            print("Welcome to TIC TAC TOE ! Let's start playing!")
            print("The first to play is player O")
            display_board()
            player_input()
            update_lines()
            display_board()
            switch_player()
            moves_count()
        else:
            player_input()
            update_lines()
            display_board()
            check_win()
            if end == 0:
                switch_player()
                moves_count()


play()

