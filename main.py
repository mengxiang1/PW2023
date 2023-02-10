import numpy as np
import pygame
from constants import *

class Gomoku:
    def __init__(self, board_size=15):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=np.int_)
        self.players = {1: "Black", -1: "White"}
        self.current_player = 1
        self.max_depth = 2  # maximum depth for minimax
        self.ended = False
    
    def print_board(self):
        for _, row in enumerate(self.board):
            print(" ".join([str(cell) for cell in row]).replace("-1", "2"))
    
    def play_move(self, x, y):
        if self.board[x][y] != 0:
            print("Illegal move. Cell already occupied.")
            return False
        self.board[x][y] = self.current_player
        if self.check_win():
            print("Player %s wins!" % self.players[self.current_player])
            self.ended = True 
        self.current_player *= -1
        return True
    def check_win(self):
        board = self.board
        player = self.current_player
        temp = board.copy()
        temp[temp != player] = 0
        temp[temp == player] = 1
        print(temp)
        for i in np.lib.stride_tricks.sliding_window_view(temp, (5, 5)):
            for window in i:
                for win in DIAGONALS:
                    if (window & win == win).all():
                        return True
        for i in np.lib.stride_tricks.sliding_window_view(temp, (1, 5)):
            for window in i:
                for win in HORIZONTAL:
                    if (window & win == win).all():
                        return True
        for i in np.lib.stride_tricks.sliding_window_view(temp, (5, 1)):
            for window in i:
                for win in VERTICAL:
                    if (window & win == win).all():
                        return True
        return False

class GameUI:
    def __init__(self) -> None:     
        #initialize pygame (required)
        pygame.init()

        #game logic
        self.game = Gomoku()

        #ui setup
        self.screen = pygame.display.set_mode((720, 640))
        self.board_length = 560
        self.board = pygame.Surface((self.board_length, self.board_length))
        

        #loop setup
        self.clock = pygame.time.Clock()
        self.mouse_pos = (0, 0)

        #styling
        self.screen.fill(GREY)
        self.board.fill(BLACK)
        self.board.fill(BROWN, self.board.get_rect().inflate(-2, -2))

        #draw lines
        for i in range(0, 14):
            pygame.draw.line(self.board, BLACK, (i*self.board_length/14, 0), (i*self.board_length/14, self.board_length))
            pygame.draw.line(self.board, BLACK, (0, i*self.board_length/14), (self.board_length, i*self.board_length/14))

        #center the board
        self.board_rect = self.board.get_rect()
        self.board_rect.center = self.screen.get_rect().center
        self.screen.blit(self.board, self.board_rect)

    def move(self, x, y):
        if self.game.play_move(x, y):
            print("MOVED")
            
            pygame.draw.circle(self.screen, BLACK if self.game.current_player == -1 else WHITE, (self.board_rect.topleft[0] + self.board_length // 14 * x, self.board_rect.topleft[1] + self.board_length // 14 * y), 15)

    def loop(self):
        #cursor position calc
        self.mouse_pos = (max(min(self.board_length, pygame.mouse.get_pos()[0] - (self.screen.get_width() - self.board_length)//2), 0), max(min(self.board_length, pygame.mouse.get_pos()[1] - (self.screen.get_height() - self.board_length)//2), 0))
        self.current_grid = tuple([(i + self.board_length // 30) // (self.board_length // 14) for i in self.mouse_pos])

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.move(*self.current_grid)
        #loop stuff
        self.clock.tick()
        pygame.display.update()

        print(self.mouse_pos, self.current_grid)

    


# game = Gomoku()
# while not game.ended:
#     game.play_move(*list(map(int, input("Enter coords: ").split())))
#     game.print_board()

game = GameUI()
while not game.game.ended:
    game.loop()