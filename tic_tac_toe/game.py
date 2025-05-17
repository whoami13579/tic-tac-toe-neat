from .piece import Piece
from .board import Board
import pygame


pygame.init()

class Game:
    BLACK = (0, 0, 0)

    def __init__(self, window: pygame.Surface, width: int, height: int):
        self.__window = window
        self.__width = width
        self.__height = height
        self.__board = Board()
        self.__pieces: list[Piece] = []
        self.__circle: bool = True
        self.__bitBoard = [[0 for i in range(3)] for j in range(3)]
        self.__run = True

    def getRun(self)->bool:
        return self.__run
    
    def draw(self):
        self.__board.draw(self.__window)

        for piece in self.__pieces:
            piece.draw(self.__window)
        
        pygame.display.flip()
    
    def __getPosition(self) -> list[int, int]:
        current_pos = pygame.mouse.get_pos()
        converted_x = int(current_pos[0] / (self.__width // 3))
        converted_y = int(current_pos[1] / (self.__height // 3))

        return converted_x, converted_y

    def addPiece(self)->int:
        """
        This function attempts to add a new piece to the game board. It returns:

        - 0 if the piece could not be added (failure).
        - 1 if the piece was successfully added to the board.
        - 2 if the game ends with a "O" win.
        - 3 if the game ends with an "X" win.
        - 4 if the game ends in a draw.
        """

        x, y = self.__getPosition()

        if self.__bitBoard[x][y] != 0:
            return 0

        self.__bitBoard[x][y] = 1 if self.__circle else -1
        self.__pieces.append(Piece(self.__circle, x, y, self.__width, self.__height))
        self.__circle = not self.__circle
        
        return self.check()
    
    def check(self)->int:
        """
        This function attempts to check the status of the game board. It returns:

        - 1 if the piece was successfully added to the board.
        - 2 if the game ends with a "O" win.
        - 3 if the game ends with an "X" win.
        - 4 if the game ends in a draw.
        """
        b = self.__bitBoard

        if b[0][0] == b[0][1] == b[0][2] == 1 or \
        b[1][0] == b[1][1] == b[1][2] == 1 or \
        b[2][0] == b[2][1] == b[2][2] == 1 or \
        b[0][0] == b[1][0] == b[2][0] == 1 or \
        b[0][1] == b[1][1] == b[2][1] == 1 or \
        b[0][2] == b[1][2] == b[2][2] == 1 or \
        b[0][0] == b[1][1] == b[2][2] == 1 or \
        b[0][2] == b[1][1] == b[2][0] == 1:
            self.__run = False
            print("O wins")
            return 2
        elif b[0][0] == b[0][1] == b[0][2] == -1 or \
        b[1][0] == b[1][1] == b[1][2] == -1 or \
        b[2][0] == b[2][1] == b[2][2] == -1 or \
        b[0][0] == b[1][0] == b[2][0] == -1 or \
        b[0][1] == b[1][1] == b[2][1] == -1 or \
        b[0][2] == b[1][2] == b[2][2] == -1 or \
        b[0][0] == b[1][1] == b[2][2] == -1 or \
        b[0][2] == b[1][1] == b[2][0] == -1:
            self.__run = False
            print("X wins")
            return 3
        else:
            for i in range(3):
                for j in range(3):
                    if b[i][j] == 0:
                        return 1
        
        self.__run = False
        print("Draw")
        return 4
