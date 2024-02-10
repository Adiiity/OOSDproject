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

