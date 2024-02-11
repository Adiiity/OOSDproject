# class Board:
#     def __init__(self, rows, cols) -> None:
#         pass

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

# Example usage
board = Board()
board.print_board()
