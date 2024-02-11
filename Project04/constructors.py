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
    hotelChains = ["American", "Continental", "Festival", "Imperial",
        "Sackson", "Tower", "Worldwide"]

    def __init__(self,hotel_name) -> None:
        #valid hotel names
        # self.hotelChains = ["American", "Continental", "Festival", "Imperial",
        # "Sackson", "Tower", "Worldwide"]

        #Check for name before creating
        if hotel_name not in self.hotelChains:
            raise NameError("Hotel must be a valid chain!")

        self.hotel_name=hotel_name

        # # dict to store hotels and the list of tiles associated with them.
        # self.occupied_hotels = {}

        for hotels in self.hotelChains:
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
        print(f"The tiles associated  with {hotel_name} -> ",occupied_hotels[hotel_name])
        return occupied_hotels[hotel_name]





class Tile:
    def __init__(self, row, col):
        if not ('A' <= row.upper() <= 'I'):
            raise ValueError("Row must be a letter from A to I.")
        if not (1 <= int(col) <= 12):
            raise ValueError("Column must be a number from 1 to 12.")

        self.row = row.upper()  # Ensures row is uppercase
        self.col = int(col)  # Ensures col is an integer

    def get_col_number(self):
        # Column is already validated as an integer from 1 to 12, subtract 1 for 0-based indexing
        return self.col - 1

    def get_row_number(self):
        # Convert row letter (validated as A to I) to 0-based index
        return ord(self.row) - ord('A')
