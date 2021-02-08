###checkers yay boys
import pygame
pygame.init()


width = 800
height = 800

win = pygame.display.set_mode((width,height))

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
beige = [245,245,220]

class Board:
  
	def __init__(self,player1,player2, color1, color2, width = 8, height = 8):
    	self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.board = [[None]*width for i in range(height)]
		#####Save board as each tile is a number, 1 is top left 
        
		for x in range(self.width):
          	for y in range(self.height):
              	xparity = x % 2
                yparity = y % 2
              	if (xparity != 0):
                  	if yparity != 0:
                    	self.board[x][y] = Tile(self.color1)
                    else:
                      	self.board[x][y] = Tile(self.color2)
                else:
                  	if yparity != 0:
                      	self.board[x][y] = Tile(self.color2)
                    else:
                      	self.board[x][y] = Tile(self.color1)
                        
        '''for y in range(self.height-3, self.height):
          	for x in range(self.width):
              if self.board[x][y]'''
        

                        
class Tile:
  
  	def __init__(self,color,piece = None):
      	self.color = color
        self.piece = piece
        
class Piece:
  	
    def __init__(self, player,up =False, down = False,  king = False):
      	self.player = player
        self.up = up
        self.down = down
        self.king = king
      
      
class Player:
  
  	def __init__(self, direction, color):
      
      	self.color = color
        self.direction = direction

player1 = Player('up', red)
player2 = Player('down', black)
board = Board(player1,player2,black, beige)

print(board.board)
      
