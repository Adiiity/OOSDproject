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