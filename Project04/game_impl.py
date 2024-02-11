from constructors import Board,Tile,Hotel
class Game:
    def __init__(self) -> None:
        self.board=Board()
        self.occupied_tiles={}
        self.occupied_hotels = {}
        self.availableHotels = Hotel.hotelChains
        self.row=Tile.get_row_number()
        self.col=Tile.get_col_number()
        self.tile=Tile.create_tile()
        # pass

    def singleton(self,row,col):
        # self.row=row
        # tile=Tile(l)
        # row = tile.get_row_number()
        # col = tile.get_col_number()
        print(f"row: {self.row} col: {self.col}")

        if 0 <= row < self.board.rows and 0 <= col < self.board.cols:
            if self.board.board_matrix[row][col] == 0:  #checking if the tile is unoccupied
                self.board.board_matrix[row][col] = 1
                self.occupied_tiles[self.tile] = "hotelname"  #for now just keeping the value as hotelnamme
                # print(f"occupied tiles: {self.occupied_tiles}")
                # self.board.print_board()
                # print("TILE Row",tile.row)
                # print("TILE Col",tile.col)
                # print("TILE Label",tile.label)
            else:
                            print("Error: Tile is already played.")
        else:
              print("Error: Invalid Tile")
        pass

    def founding(self,row,column,label, board):
        board = self.board.board_matrix
        total_rows = len(board)
        total_cols = len(board[0])
        tile=Tile(label)
        current_row_num = tile.get_row_number()
        current_col_num = tile.get_col_number()

        #  neighbors indices
        delRow = [ -1, 0, +1, 0 ]
        delCol = [ 0, +1, 0, -1 ]


        # task 1: Check if the given grid is empty else return error.
        if(board[current_row_num][current_col_num] ==1):
            return "Tile is already occupied"

        #  TASK 2: check if there is  any tile as neighbor to the given grid.
        else:
            neighbour_tiles = []
            for i in range(4):
                # adding valid indices only to neighbor tiles
                next_row =  current_row_num+delRow[i]
                next_col =  current_col_num+delCol[i]
                if(next_row>=0 and next_row<total_rows and next_col>=0 and next_col<total_cols):
                        neighbour_tiles.append((next_row,next_col))

            self.board.print_board()
            print("GIVEN", current_row_num, current_col_num)
            print("Neighbor Tiles:",neighbour_tiles)


            for i,j in neighbour_tiles:
                row = i
                column = j
                isSingleTile =self.singleTile(row,column,delRow,delCol,board,total_rows,total_cols)

                if isSingleTile:
                    board[row][column] = 1
                    if label in self.availableHotels:
                        print("Available Hotels: ",self.availableHotels)
                        self.availableHotels.remove(label)
                    else:
                        print("hotel removed")



            #  get the list of hotel chains from hotel class.

            # remove that hotel from the list if it exists.

            # if the hotel is not there just place the tile.

    def singleTile(self,row,column,delRow,delCol,board,total_rows,total_cols):
        for i in range(4):
            next_row =  row+delRow[i]
            next_col =  column+delCol[i]
            if(next_row>=0 and next_row<total_rows and next_col>=0 and next_col<total_cols):
                if(board[next_row][next_col]!=0):
                    return False

        return True








game=Game()
# game.singleton("4F")

game.singleton("4E")
game.singleton("5F")
ans = game.founding(4,"F","4F",game.board)
print(ans)