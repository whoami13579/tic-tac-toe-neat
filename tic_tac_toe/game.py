from .piece import Piece
from .board import Board
import pygame


pygame.init()

class Game:
    BLACK = (0, 0, 0)

    def __init__(self, window: pygame.Surface, width: int, height: int):
        self.window = window
        self.width = width
        self.height = height
        self.board = Board()
        self.pieces: list[Piece] = []
        self.circle: bool = True
        self.bitBoard = [[0 for i in range(3)] for j in range(3)]

    def draw(self):
        self.board.draw(self.window)

        for piece in self.pieces:
            piece.draw(self.window)
        
        pygame.display.flip()
    
    def __getPosition(self) -> list[int, int]:
        current_pos = pygame.mouse.get_pos()
        converted_x = int(current_pos[0] / (self.width // 3))
        converted_y = int(current_pos[1] / (self.height // 3))

        return converted_x, converted_y

    def addPiece(self)->bool:
        x, y = self.__getPosition()

        if self.bitBoard[x][y] != 0:
            return False

        self.bitBoard[x][y] = 1 if self.circle else -1
        self.pieces.append(Piece(self.circle, x, y, self.width, self.height))
        self.circle = not self.circle
        
        return True
