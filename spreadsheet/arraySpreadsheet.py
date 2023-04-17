from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.data = []
        self.c_row = 0
        self.c_col = 0


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        for lCell in lCells:
            if (lCell.row >= self.c_row):
                for i in range(self.c_row, lCell.row + 1):
                    self.data.append([])
    
                self.c_row = lCell.row + 1

            if (lCell.col >= self.c_col):
                self.c_col = lCell.col + 1

            self.data[lCell.row].append(lCell)

            self.data[lCell.row] = sorted(self.data[lCell.row],
                key=lambda cell: cell.col)


    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        self.data.append([])
        self.c_row += 1
        
        return True


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        self.c_col += 1

        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        if (rowIndex > 0 and rowIndex < self.c_row):
            for i in range(rowIndex, len(self.data)):
                for j in range(len(self.data[i])):
                    self.data[i][j].row += 1
                    
            self.data.insert(rowIndex, [])
            self.c_row += 1

            return True

        return False


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        if (colIndex > 0 and colIndex < self.c_col):
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    if (self.data[i][j].col >= colIndex):
                        self.data[i][j].col += 1

            self.c_col += 1

            return True

        return False


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if (rowIndex < self.c_row and colIndex < self.c_col):
            for i in range(len(self.data[rowIndex])):
                if (self.data[rowIndex][i].col == colIndex):
                    self.data[rowIndex][i].val = value

                    return True
            
            new_cell = Cell(rowIndex, colIndex, value)
            self.data[rowIndex].append(new_cell)
            self.data[rowIndex] = sorted(self.data[rowIndex],
                key=lambda cell: cell.col)

            return True

        return False


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        return self.c_row


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        return self.c_col



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        result : [(int, int)] = []
        
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if (self.data[i][j].val == value):
                    result.append((self.data[i][j].row,self.data[i][j].col))

        return result



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        result : [Cell] = [] 

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                result.append(self.data[i][j])

        return result
