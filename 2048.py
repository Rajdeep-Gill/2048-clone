import numpy as np
import random
import os
from regex import F
from termcolor import colored, cprint

COLORS = {2: 'red', 4: 'blue', 8: 'green', 16: 'yellow', 32: 'magenta', 64: 'cyan', 128: 'white', 256: 'black', 512: 'orange', 1024: 'purple', 2048: 'pink'}

class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size))

    def get_board(self):
        return self.board
    
    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                if j % self.size != 0:
                    print("| ", end="")

                if self.board[i][j] != 0:
                    cprint(int(self.board[i][j]), color=COLORS[int(self.board[i][j])], end=" ")
                else:
                    print(" ", end=" ")
            print()
            if i < self.size - 1:
                print('--+---+---+--')

    def add_piece(self, position, pieceValue):
        row, col = position
        self.board[row][col] = pieceValue

    def clearBoard(self):
        self.board = np.zeros((self.size, self.size))

    def peiceCount(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    count += 1
                    
        return count


class Piece:
    def __init__(self, ):
        self.value = 2 if random.random() < 0.8 else 4
        self.position = (0, 0)

    def getPosition(self, Board):
        validPositions = []
        for i in range(Board.size):
            for j in range(Board.size):
                if Board.board[i][j] == 0:
                    validPositions.append((i, j))
        self.position = random.choice(validPositions)
    
gameBoard = Board(4)


peices = []

def startGame(peices):
    gameBoard.clearBoard()
    for i in range(2):
        newPeice = Piece()
        newPeice.getPosition(gameBoard)
        peices.append(newPeice)
        gameBoard.add_piece(peices[i].position, peices[i].value)

    cprint("Welcome to 2048!\n", color='yellow', attrs=['bold'] )
    gameBoard.printBoard()

startGame(peices)

def addPiece():
    newPeice = Piece()
    newPeice.getPosition(gameBoard)
    peices.append(newPeice)
    gameBoard.add_piece(peices[-1].position, peices[-1].value)

def moveUp(score):
    moved = False
    for tries in range(5):
        for col in range(gameBoard.size - 1, -1, -1):
            for row in range(gameBoard.size - 1, 0, -1):
                if gameBoard.board[row][col] == 0:
                    continue
                elif gameBoard.board[row][col] == gameBoard.board[row - 1][col] and tries < 2:
                    gameBoard.board[row - 1][col] = gameBoard.board[row][col] * 2
                    gameBoard.board[row][col] = 0
                    moved = True
                    score += gameBoard.board[row - 1][col]
                    break
                elif gameBoard.board[row][col] != 0:
                    if gameBoard.board[row - 1][col] == 0:
                        gameBoard.board[row - 1][col] = gameBoard.board[row][col]
                        gameBoard.board[row][col] = 0
                        moved = True
    return moved, score

def moveDown(score):
    moved = False
    for tries in range(5):
        for col in range(gameBoard.size):
            for row in range(gameBoard.size - 1):
                if gameBoard.board[row][col] == 0:
                    continue
                elif gameBoard.board[row][col] == gameBoard.board[row + 1][col] and tries < 2:
                    gameBoard.board[row + 1][col] = gameBoard.board[row][col] * 2
                    gameBoard.board[row][col] = 0
                    moved = True
                    score += gameBoard.board[row + 1][col]
                    break
                elif gameBoard.board[row][col] != 0:
                    if gameBoard.board[row + 1][col] == 0:
                        gameBoard.board[row + 1][col] = gameBoard.board[row][col]
                        gameBoard.board[row][col] = 0
                        moved = True
                        break
    return moved, score

def moveLeft(score):
    moved = False
    for tries in range(5):
        for row in range(gameBoard.size):
            for col in range(gameBoard.size - 1, 0, -1):
                if gameBoard.board[row][col] == 0:
                    continue
                elif gameBoard.board[row][col] == gameBoard.board[row][col - 1] and tries < 2:
                    gameBoard.board[row][col - 1] = gameBoard.board[row][col] * 2
                    gameBoard.board[row][col] = 0
                    moved = True
                    score += gameBoard.board[row][col - 1]
                    break
                elif gameBoard.board[row][col] != 0:
                    if gameBoard.board[row][col - 1] == 0:
                        gameBoard.board[row][col - 1] = gameBoard.board[row][col]
                        gameBoard.board[row][col] = 0
                        moved = True
                        break
    return moved, score

def moveRight(score):
    moved = False
    for tries in range(5):
        for row in range(gameBoard.size):
            for col in range(gameBoard.size - 1):
                if gameBoard.board[row][col] == 0:
                    continue
                elif gameBoard.board[row][col] == gameBoard.board[row][col + 1] and tries < 2:
                    gameBoard.board[row][col + 1] = gameBoard.board[row][col] * 2
                    gameBoard.board[row][col] = 0
                    moved = True
                    score += gameBoard.board[row][col + 1]
                    break
                elif gameBoard.board[row][col] != 0:
                    if gameBoard.board[row][col + 1] == 0:
                        gameBoard.board[row][col + 1] = gameBoard.board[row][col]
                        gameBoard.board[row][col] = 0
                        moved = True
                        break
    return moved, score

def printToConsole():
    os.system('CLS')
    cprint("Welcome to 2048!\n", color='yellow', attrs=['bold'] )
    gameBoard.printBoard()
    scoreStr = "Score: " + str(score)
    cprint(scoreStr, color='red', attrs=['bold'] )


gameOver = False
moveList = ['w', 'a', 's', 'd']
score = 0
while not gameOver:
    moveStr = ''
    for i in moveList:
        moveStr += i + ', '
    moveStr = moveStr[:len(moveStr) - 2]
    moveStr = moveStr.upper()
    moveStr += ' to move: '
    validMove = input(moveStr)
    validMove = validMove.lower()

    while validMove not in moveList:
        validMove = input(moveStr)
    didMove = False

    if validMove == 'w':
        didMove, score = moveUp(score)
    elif validMove == 'a':
        didMove, score = moveLeft(score)
    elif validMove == 's':
        didMove, score = moveDown(score)
    elif validMove == 'd':
        didMove, score = moveRight(score)

    #after every move, make a new peice

    peicesOnBoard = gameBoard.peiceCount()
    if didMove:
        moveList = ['w', 'a', 's', 'd']
        if peicesOnBoard < gameBoard.size ** 2:
            addPiece()
            printToConsole()
        elif len(moveStr) == 0:
            gameOver = True
    else:
        if validMove in moveList:
            moveList.remove(validMove)
        print("Can't move in that direction")


print("Game Over")
print('test')