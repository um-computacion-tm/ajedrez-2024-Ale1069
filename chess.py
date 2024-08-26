class Chess:
    def __init__(self, board):
        self.board = board()
        self.turn = "WHITE"

    def move(
        self,    
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        #validar coordenadas
        piece = self.board.get_piece(from_row, from_col, to_row, to_col)
        self.change_turn()
    #cambiar turno
    def change_turn(self):    
        if self.__turn__ == "WHITE":
            self.__turn__ == "BLACK"
        else:
            self.__turn__ == "BLACK"