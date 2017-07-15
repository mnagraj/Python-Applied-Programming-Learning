# Tic Tac Toe

import random

#printing the game board
def boardDraw(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Selecting the players symbol choice X or O
def inputPlayerLetter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Which one do you want X or O : ?')
        letter = input().upper()


    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

#Selecting the First player to move

def whoIsFirst():

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

#aksing for another game

def repeatGame():

    print('Will you like to play one more game : (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter
#calculating the who is the winner between two players
def pickWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def pickBoard(board):

    copyBoard = []

    for i in board:
        copyBoard.append(i)

    return copyBoard

def checkSpace(board, move):

    return board[move] == ' '
#entering the player choice through input
def pickPlayerChoice(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not checkSpace(board, int(move)):
        print('Plz Select the Numbers that are not choosen yet(1-9)')
        move = input()
    return int(move)
#choosing from available moves left
def getAnyMoveInList(board, movesList):

    movesPossible = []
    for i in movesList:
        if checkSpace(board, i):
            movesPossible.append(i)

    if len(movesPossible) != 0:
        return random.choice(movesPossible)
    else:
        return None
#randomly generated computer move
def randomMovebyComputer(board, letterOfComputerChoice):

    if letterOfComputerChoice== 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy =pickBoard(board)
        if checkSpace(copy, i):
            makeMove(copy, letterOfComputerChoice, i)
            if pickWinner(copy, letterOfComputerChoice):
                return i


    for i in range(1, 10):
        copy = pickBoard(board)
        if checkSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if pickWinner(copy, playerLetter):
                return i


    move = getAnyMoveInList(board, [1, 3, 7, 9])
    if move != None:
        return move


    if checkSpace(board, 5):
        return 5


    return getAnyMoveInList(board, [2, 4, 6, 8])

def checkBoardStatus(board):

    for i in range(1, 10):
        if checkSpace(board, i):
            return False
    return True


print('Tic Tac Toe Game :')

while True:

    theBoard = [' '] * 10
    playerLetter, letterOfComputerChoice = inputPlayerLetter()
    turn = whoIsFirst()

    playingIsUnder= True

    while playingIsUnder:
        if turn == 'player':
            # Player's turn.
            boardDraw(theBoard)
            move = pickPlayerChoice(theBoard)
            makeMove(theBoard, playerLetter, move)

            if pickWinner(theBoard, playerLetter):
                boardDraw(theBoard)
                print('You won the game!')
                playingIsUnder = False
            else:
                if checkBoardStatus(theBoard):
                    boardDraw(theBoard)
                    print('game tied!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = randomMovebyComputer(theBoard,letterOfComputerChoice)
            makeMove(theBoard,letterOfComputerChoice, move)

            if pickWinner(theBoard, letterOfComputerChoice):
                boardDraw(theBoard)
                print('Sorry ! Computer won !! ')
                gameIsPlaying = False
            else:
                if checkBoardStatus(theBoard):
                    boardDraw(theBoard)
                    print('game tied!')
                    break
                else:
                    turn = 'player'

    if not repeatGame():
        break