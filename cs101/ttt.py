
# Game board -  Game State


def createBoard():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return board

def printBoard(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print(f"---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print(f"---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")



def userMove(board,player):
    move = input("Enter your move. (1-9): ")
    if move == "1":
        board[0][0] = player
    elif move == "2":
        board[0][1] = player
    elif move == "3":
        board[0][2] = player
    elif move == "4":
        board[1][0] = player
    elif move == "5":
        board[1][1] = player
    elif move == "6":
        board[1][2] = player
    elif move == "7":
        board[2][0] = player
    elif move == "8":
        board[2][1] = player
    elif move == "9":
        board[2][2] = player
    else:
        print(f"Error: Invalid move. '{move}' .")


def checkForWinner(board,player):
    
    # check rows
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return player
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return player
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return player

    #check columns
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return player
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return player
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return player

    #check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return player
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return player
    

    # checking tie
    if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[2][0] != " " and board[2][1] != " " and board[2][2] != " " :
        return "cat"



# Main Programming
board = createBoard()
printBoard(board)
player = "x"
winner = None

# Game Loop

while winner == None:
    
    # player move
    userMove(board,player)
    
    # print board
    printBoard(board)


    #check for winner
    winner = checkForWinner(board,player)

    #Switch player (toggle pattern)
    if player == "x":
        player = "o"
    else:
        player = "x"    


if winner == "cat":
    print("Tie game.")
else:
    print(f'Player "{winner}" has won the game!')       
