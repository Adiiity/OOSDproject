from constructors import Board,Tile,Hotel
class Game:
    def __init__(self) -> None:
        self.board=Board()
        self.occupied_tiles={}
        self.occupied_hotels = {}
        self.availableHotels = Hotel.hotelChains
        # self.row=Tile.get_row_number()
        # self.col=Tile.get_col_number()
        # self.tile=Tile.create_tile()
        # pass

    def singleton(self,row,col):
        # self.row=row
        tile = Tile(str(row), str(col))
        row_index, col_index = tile.get_row_number(),tile.get_col_number()
        print(f"row: {row_index} col: {col_index}")

        if 0 <= row_index < self.board.rows and 0 <= col_index < self.board.cols:
            if self.board.board_matrix[row_index][col_index] == 0:  #checking if the tile is unoccupied
                self.board.board_matrix[row_index][col_index] = 1
                self.occupied_tiles[row,col] = "hotelname"  #for now just keeping the value as hotelnamme
                print(f"occupied tiles: {self.occupied_tiles}")
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
        tile=Tile(row,column)
        current_row_num = tile.get_row_number()
        current_col_num = tile.get_col_number()

        print(current_row_num,current_col_num)
        #  neighbors indices
        delRow = [ -1, 0, +1, 0 ]
        delCol = [ 0, +1, 0, -1 ]


        # task 1: Check if the given grid is empty else return error.
        if(board[current_row_num][current_col_num] ==1):
            return {"error":"Tile is already occupied"}

        #  TASK 2: check if there is  any tile as neighbor to the given grid.
        else:
            neighbour_tiles = []
            for i in range(4):
                # adding valid indices only to neighbor tiles
                next_row =  current_row_num+delRow[i]
                next_col =  current_col_num+delCol[i]
                if(next_row>=0 and next_row<total_rows and next_col>=0 and next_col<total_cols):
                        neighbour_tiles.append((next_row,next_col))

            # self.board.print_board()
            # print("GIVEN", current_row_num, current_col_num)
            # print("BOARD VALUE ", board[current_row_num][current_col_num])
            # print("Neighbor Tiles:",neighbour_tiles)
            
            
# We must found a hotel if the neighbour single tiles are occupied. '0' tiles can be single as well, we must ignore it.
            occupied_neighbour = False
            for i,j in neighbour_tiles:
                
                row_index = i
                column_index = j
                # print(board[row_index][column_index])
                if board[row_index][column_index] != 1:
                    print("THIS NEIGHBOUR IS NOT OCCUPIED YET. SO NO FOUNDING HOTEL")
                    # return {"error": "Hotels can be found next to singly occupied tiles only"}
                    
                else:
                    occupied_neighbour = True
                    isSingleTile =self.singleTile(row_index,column_index,delRow,delCol,board,total_rows,total_cols)
                    # print("BOARD VALUE ", board[current_row_num][current_col_num])
                    if isSingleTile:
                        print("Is a single tile")
                        # board[row][column] = 1
                        if label in self.availableHotels:
                            
                            # make the given indices by user as tile
                            self.singleton(row,column)
                            # print(self.occupied_tiles)
                            if label not in self.occupied_hotels:
                                # create a key with hotel name 
                                self.occupied_hotels[label] = []
                                # add the given tile and the single tile to this key
                                self.occupied_hotels[label].append((row_index,column_index))
                                self.occupied_hotels[label].append((row,column))
                                # change occupied tiles as well add hotel label now
                                # self.occupied_tiles[row_index,column_index] = label
                                # update given row and col
                                self.occupied_tiles[row,column] = label
                                # update teh single neighbour tile
                                letter_row_ascii_number = ord('A') + row_index
                                letter_row = chr(letter_row_ascii_number)
                                self.occupied_tiles[letter_row,column_index + 1] = label
                                print(f" updated occupied tiles: {self.occupied_tiles}")
                                
                                
                                # remove the label from available hotels
                                self.availableHotels.remove(label)

                            self.board.print_board
                            # print("Available Hotels: ",self.availableHotels)
                            # print("Occupied Hotels:",self.occupied_hotels)
                            # print( "founding fucntion ends Hotel added")
                            return "founding"
                    # If there are no available hotel chains, the player can place the tile but cannot found a new hotel
                    elif label not in self.availableHotels:
                        # print("The given hotel label is not present in the available hotel chains. So adding tile only")
                        # we create and place the tile
                        self.singleton(row,column)
                        # print("founding fucntion ends Just tile added")
                        self.board.print_board()
                        return "singleton"

            if occupied_neighbour == False:
                self.board.print_board()
                return {"error": "Hotels can be found next to singly occupied tiles only"}

            #  get the list of hotel chains from hotel class.

            # remove that hotel from the list if it exists.

            # if the hotel is not there just place the tile.

    def singleTile(self,row,column,delRow,delCol,board,total_rows,total_cols):
        # print("SINGLE TILE FUNCTION")
        # print("INDICES",row,column)
        # print("CURRENT GRID NEIGHBOUR VALUE",board[row][column])
        for i in range(4):
            next_row =  row+delRow[i]
            next_col =  column+delCol[i]
            print("NEIGHBOUR", board[next_row][next_col])
            if( next_row>=0 and next_row<total_rows and next_col>=0 and next_col<total_cols ):
                if(board[next_row][next_col]!=0):
                    return False
            

        return True








game=Game()
# game.singleton("4F")

game.singleton("E",4)
# game.singleton("F",5)
# Trying to found hotel around non existent neighbour tiles i.e 0 on all 4 sides
# ans = game.founding("A",1,"American",game.board)

# Trying to found hotel around existent  tiles i.e 1 on the given row,col
# ans = game.founding("E",4,"American",game.board)


# Trying to found hotel around an existent single neighbour tiles i.e atleast 1 neighbour is single who is alone
# ans = game.founding("E",5,"American",game.board)
# print(ans)

#Trying to add a tile to a hotel lable that is not present in available hotels
# ans is added to the hotel chain AMERICAN
ans = game.founding("E",5,"American",game.board)
# Ans1 can not be added now since American wont be available
ans1 = game.founding("E",3,"American",game.board)
print(ans1)