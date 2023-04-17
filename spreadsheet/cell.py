
# -------------------------------------------------
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# -------------------------------------------------

# Class representing a cell and its value.
class Cell:
    def __init__(self, row: int, col: int, val: float):
        # a cell object has the row, column and value
        self.row = row
        self.col = col
        self.val = val

    def __str__(self) -> str:
        """
        Convert cell to a string for printing.
        """

        return "(" + str(self.row) + "," + str(self.col) + "," + "{:.2f}".format(self.val) + ")"
