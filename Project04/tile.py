#  the board is a 2d matrix that indexes from 0.
#  So each grid on the board is  holding a tile.
#  a tile is a string like [a1,a2,a3...] where a is the row and 1 is the column
#  We can decide where this tile is placed on board if we do some functionality to get indices [row][col]
# when you create a tile, its availability is set to false as this tile is going to be placed on the board
class Tile:
    def __init__(self,row :str,col :int):
        self.row=row
        self.col=col
        self.isAvailable = False
        
    def get_row_number(self,row :str):
        
        ascii_value = ord(row[0])
        ascii_value_A = ord('A')
        
        board_row_number = ascii_value-ascii_value_A
        return board_row_number
    
    def get_row_number(self,col :int):
        board_col_number = col - 1
        return board_col_number
        