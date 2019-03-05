class GameBoard(object):
    """
    Create a 2d array representation of the gameboard\n
    @param height -> Desired grid height\n
    @param width -> Desired grid width
    """

    def __init__(self, height, width, value=0):
        self.height = height
        self.width = width
        self.board = [[value] * self.height for _ in range(self.width)]


    def set_cell(self, cell, value):
        """
        Mark cell with desired value\n
        @param cell -> Array containing x and y coordinates [x,y]\n
        @param value -> Mark the cell with a specified value
        """
        self.board[cell[0]][cell[1]] = value
        

    def get_cell(self, cell):
        """
        Retrive cell from grid\n
        @return cell -> The cell value
        """
        return self.board[cell[0]][cell[1]]


    def display_game(self, title='Game Board'):
        """
        Display formatted grid in the console\n
        @param grid -> Grid you would like to display\n
        @param title -> Custom title for display
        """

        new_grid = []
        row = []
        for y in xrange(self.height):
            for x in xrange(self.width):
                if len(row) == self.width:
                    row = []
                char = self.board[x][y]
                row.append(char)
            new_grid.append(row)
        print('Game: %s' % title)
        for row in new_grid:
            print(row)
            