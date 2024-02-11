class Board:
    def __init__(self):
        self.rows = 9
        self.cols = 12
        self.board_matrix = self.init_board()

    def init_board(self):
        board_matrix = []
        for row in range(self.rows):
            row_list = []
            for col in range(self.cols):
                row_list.append(0)
            board_matrix.append(row_list)
        return board_matrix

    def print_board(self):
        for row in self.board_matrix:
            print(' '.join(map(str, row)))


class Hotel:
    def __init__(self,hotel_name) -> None:
        #valid hotel names
        hotelChains = ["American", "Continental", "Festival", "Imperial",
        "Sackson", "Tower", "Worldwide"]

        #Check for name before creating
        if hotel_name not in hotelChains:
            raise NameError("Hotel must be a valid chain!")

        self.hotel_name=hotel_name

        # dict to store hotels and the list of tiles associated with them.
        self.occupied_hotels = {} 
        
        for hotels in hotelChains:
            self.occupied_hotels[hotels] = []


    def found_hotel(self, hotel_name, tile):
        hotel = hotel_name


    def merge_hotel():
        pass

    def grow_hotel():
        # add a new tile to the list under the hotel name
        pass
    def get_hotels_data(self,hotel_name,occupied_hotels):
        # invalid hotel name.
        if hotel_name not in occupied_hotels:
            raise NameError("Hotel must be a valid chain!")
        
        return occupied_hotels[hotel_name]
            

        
        

class Tile:
    def __init__(self,label):
        # self.row=row
        # self.col=col
        self.label = label
        self.col = int(label[:-1])  # taking the number part
        self.row = label[-1]  # taking the letter part

    # def return_label(self):
    #     return self.label

    def get_col_number(self):


        board_col_number = self.col - 1
        return board_col_number

    def get_row_number(self):

        ascii_value = ord(self.row[0])
        ascii_value_A = ord('A')

        board_row_number = ascii_value-ascii_value_A
        return board_row_number
