class Board:
    def __init__(self, rows, cols) -> None:
        self.rows=rows
        self.cols=cols
        self.board_matrix=[]
        pass

        for row in range(rows):
            row_list=[]
            for col in range(cols):
                row_list.append("0")
            self.board_matrix.append(row_list)


class Hotel:
    def __init__(self,hotel_name) -> None:
        #valid hotel names
        hotelChains = ["American", "Continental", "Festival", "Imperial",
        "Sackson", "Tower", "Worldwide"]

        #Check for name before creating
        if hotel_name not in hotelChains:
            raise NameError("Hotel must be a valid chain!")

        self.hotel_name=hotel_name
        self.tiles_list=[] #figure out how to do this? a list of tiles for each hotel chain


    def found_hotel(self, hotel_name, tile):
        hotel = hotel_name


    def merge_hotel():
        pass

    def grow_hotel():
        # add a new tile to the list under the hotel name
        pass


class Tile:
    def __init__(self,row :int,col :str):
        self.row=row
        self.col=col

        
    def get_row_number(self,row :int):
        
        
        board_row_number = row - 1
        return board_row_number
    
    def get_col_number(self,col :str):
        
        ascii_value = ord(col[0])
        ascii_value_A = ord('A')
        
        board_col_number = ascii_value-ascii_value_A
        return board_col_number
        