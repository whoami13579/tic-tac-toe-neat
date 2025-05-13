from .piece import Piece
from .board import Board
import pygame


pygame.init()

class Game:
    BLACK:tuple = (0, 0, 0)

    def __init__(self, window: pygame.Surface, width: int, hight: int):
        self.window: pygame.Surface = window
        self.window_width: int = width
        self.window_width: int = hight
        self.board:Board = Board()
        self.pieces: list[Piece] = []

    def draw(self):
        window = self.window
        board:Board = self.board
        pieces: list[Piece] = self.pieces

        board.draw(window)
        
        # for piece in pieces:
            # piece.draw(window)
        
        pygame.display.flip()
