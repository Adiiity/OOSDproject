from new_constructors import Board,Tile,Hotel
class Game:
    def __init__(self,board_data) -> None:

        self.board=Board(board_data)

        self.occupied_tiles=self.board.played_tiles.copy()
        self.occupied_hotels = self.board.played_hotels.copy()
        self.availableHotels = Hotel.valid_hotels
        # print("OCCUPIED HOTELS START",self.occupied_hotels)
        # print("STATE BEFORE UPDATE",self.availableHotels)
        copyAvailableHotels = []
        for hotel in self.availableHotels:
            if hotel not in self.occupied_hotels:
                copyAvailableHotels.append(hotel)
        
        self.availableHotels = copyAvailableHotels

        # print("STATE AFTER UPDATE",self.availableHotels)
        # self.row=Tile.get_row_index()
        # self.col=Tile.get_col_index()
        # self.tile=Tile.create_tile()

    def singleton(self,row,col):
        # self.row=row
        tile = Tile(str(row), str(col))
        row_index, col_index = tile.get_row_index(),tile.get_col_index()
        # print(f"row: {row_index} col: {col_index}")

        if 0 <= row_index < self.board.rows and 0 <= col_index < self.board.cols:
            if self.board.board_matrix[row_index][col_index] == 0:  #checking if the tile is unoccupied
                self.board.board_matrix[row_index][col_index] = 1
                self.occupied_tiles[row_index,col_index] = None  #for now just keeping the value as None
                # print("Singleton done")
                # print(f"occupied tiles: {self.occupied_tiles}")
                # self.board.print_board()
                # print("TILE Row",tile.row)
                # print("TILE Col",tile.col)
                # print("TILE Label",tile.label)
            else:
                print("Error: Tile is already played.")
        else:
              print("Error: Invalid Tile")


    def founding(self,row,column,label, board):
        

        game_board = self.board.board_matrix
        total_rows = len(game_board)
        total_cols = len(game_board[0])
        tile=Tile(row,column)
        current_row_num = tile.get_row_index()
        current_col_num = tile.get_col_index()

        print(current_row_num,current_col_num)
        #  neighbors indices
        delRow = [ -1, 0, +1, 0 ]
        delCol = [ 0, +1, 0, -1 ]


        # task 1: Check if the given grid is empty else return error.
        if(game_board[current_row_num][current_col_num] ==1):
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
                if game_board[row_index][column_index] != 1:
                    print("THIS NEIGHBOUR IS NOT OCCUPIED YET. SO NO FOUNDING HOTEL")
                    # return {"error": "Hotels can be found next to singly occupied tiles only"}

                else:
                    occupied_neighbour = True
                    isSingleTile =self.singleTile(row_index,column_index,delRow,delCol,game_board,total_rows,total_cols)
                    # print("BOARD VALUE ", board[current_row_num][current_col_num])
                    print("OCCUPIED HOTElS befor check", self.occupied_hotels)
                    print("Available HOTElS befor check", self.availableHotels)
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
                                letter_row_ascii_number = ord('A') + row_index
                                letter_row = chr(letter_row_ascii_number)
                                # add the given tile and the single tile to this key
                                self.occupied_hotels[label].append((letter_row,column_index + 1))
                                self.occupied_hotels[label].append((row,column))
                                print(f" updated occupied hotels: {self.occupied_hotels}")
                                # change occupied tiles as well. add hotel label now
                                # self.occupied_tiles[row_index,column_index] = label
                                # update given row and col
                                self.occupied_tiles[row,column] = label
                                # update teh single neighbour tile

                                self.occupied_tiles[letter_row,column_index + 1] = label
                                print(f" updated occupied tiles: {self.occupied_tiles}")


                                # remove the label from available hotels
                                self.availableHotels.remove(label)

                            self.board.print_board()
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

    def singleTile(self,row,column,delRow,delCol,game_board,total_rows,total_cols):
        # print("SINGLE TILE FUNCTION")
        # print("INDICES",row,column)
        # print("CURRENT GRID NEIGHBOUR VALUE",board[row][column])
        for i in range(4):
            next_row =  row+delRow[i]
            next_col =  column+delCol[i]
            print("NEIGHBOUR", game_board[next_row][next_col])
            if( next_row>=0 and next_row<total_rows and next_col>=0 and next_col<total_cols ):
                if(game_board[next_row][next_col]!=0):
                    return False


        return True

    def growing(self, row, col, hotel_name):
        tile = Tile(str(row), str(col))
        row_index, col_index = tile.get_row_index(), tile.get_col_index()
        tile_tuple = (row_index, col_index)  # Use 0-based indices for internal tracking
        print(f"Occupied tiles before: {self.occupied_tiles}")

        # Check if the tile is already played
        if tile_tuple in self.occupied_tiles:
            # If the tile is already associated with a hotel, raise an error
            if self.occupied_tiles[tile_tuple] is not None:
                print("Error: Tile is already played and is in a hotel chain.")
                return

            # If the tile exists but not associated with a hotel, update its association
            self.occupied_tiles[tile_tuple] = hotel_name
        else:
            # If the tile is not played, add it as a new tile associated with the given hotel
            self.occupied_tiles[tile_tuple] = hotel_name
            self.board.board_matrix[row_index][col_index] = 1  # Mark the tile as placed
            self.board.print_board()

        # Update the occupied hotels
        if hotel_name not in self.occupied_hotels:
            self.occupied_hotels[hotel_name] = [tile_tuple]
        else:
            if tile_tuple not in self.occupied_hotels[hotel_name]:
                self.occupied_hotels[hotel_name].append(tile_tuple)

        print(f"Occupied tiles update: {self.occupied_tiles}")
        print(f"Tile added to {hotel_name}: {self.occupied_hotels}")




# To set up out board
board_data = {
    "tiles": [
        {"row": "A", "column": 1, "hotel_name": "Continental"},
        {"row": "B", "column": 2, "hotel_name": None},
        {"row": "B", "column": 3, "hotel_name": "Continental"}
    ],
    "hotels": [
        {"hotel": "Continental", "tiles": [{"row": "A", "column": 1},{"row": "B", "column": 3}]}
    ]
}

game=Game(board_data)
# game.singleton("A",5)




# game=Game()
# # game.singleton("4F")

game.singleton("E",4)
# # game.singleton("F",5)
# # Trying to found hotel around non existent neighbour tiles i.e 0 on all 4 sides
# # ans = game.founding("A",1,"American",game.board)

# # Trying to found hotel around existent  tiles i.e 1 on the given row,col
# # ans = game.founding("E",4,"American",game.board)


# # Trying to found hotel around an existent single neighbour tiles i.e atleast 1 neighbour is single who is alone
ans = game.founding("E",5,"Sackson",game.board)
print(ans)

# #Trying to add a tile to a hotel lable that is not present in available hotels
# # ans is added to the hotel chain AMERICAN
# ans = game.founding("E",5,"American",game.board)
# # Ans1 can not be added now since American wont be available
# ans1 = game.founding("E",3,"American",game.board)
# print(ans1)

