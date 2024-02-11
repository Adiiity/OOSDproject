from constructors import Board,Tile
class Game:
    def __init__(self) -> None:
        self.board=Board()
        self.occupied_tiles={}
        # pass

    def singleton(self,label):
        tile=Tile(label)
        row = tile.get_row_number()
        col = tile.get_col_number()
        print(f"row: {row} col: {col}")

        if 0 <= row < self.board.rows and 0 <= col < self.board.cols:
            if self.board.board_matrix[row][col] == 0:  #checking if the tile is unoccupied
                self.board.board_matrix[row][col] = 1
                self.occupied_tiles[label] = "hotelname"  #for now just keeping the value as hotelnamme
                print(f"occupied tiles: {self.occupied_tiles}")
                self.board.print_board()
            else:
                            print("Error: Tile is already played.")
        else:
              print("Error: Invalid Tile")
        pass

game=Game()
game.singleton("4F")