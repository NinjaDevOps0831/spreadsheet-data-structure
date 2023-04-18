from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
import numpy as np
from scipy.sparse import csr_matrix, find


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------




class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        
        self.c_row = 0
        self.c_col = 0
        
        pass


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED
        cnt = 0
        max_row = 0
        max_col = 0
        datacount = len(lCells)
        rcv = np.zeros(shape = (3, datacount))
        for lCell in lCells:            
            rcv[0,cnt] = lCell.row
            rcv[1,cnt] = lCell.col
            rcv[2,cnt] = lCell.val
            cnt = cnt+1
            if(max_row < lCell.row):
                max_row = lCell.row
            if(max_col < lCell.col):
                max_col = lCell.col

        self.matrix = csr_matrix((rcv[2], (rcv[0], rcv[1])), shape=(max_row+1, max_col+1))
       
        self.c_row = max_row+1
        self.c_col = max_col+1
        
        pass


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        rcv = find(self.matrix)

        newrcv = np.zeros(shape = (3, len(rcv[2]) + 1))
        
        for i in range(len(rcv[2])):
            newrcv[0,i] = rcv[0][i]
            newrcv[1,i] = rcv[1][i]
            newrcv[2,i] = rcv[2][i]
        newrcv[0,len(rcv[2])] = self.c_row
        newrcv[1,len(rcv[2])] = self.c_col-1
        newrcv[2,len(rcv[2])] = 0
        self.matrix = csr_matrix((newrcv[2], (newrcv[0], newrcv[1])), shape=(self.c_row+1, self.c_col))
        
        self.c_row  = self.c_row + 1
        return True          

        pass


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        rcv = find(self.matrix)
        newrcv = np.zeros(shape = (3, len(rcv[2]) + 1))
        
        for i in range(len(rcv[2])):
            newrcv[0,i] = rcv[0][i]
            newrcv[1,i] = rcv[1][i]
            newrcv[2,i] = rcv[2][i]
        newrcv[0,len(rcv[2])] = self.c_row-1
        newrcv[1,len(rcv[2])] = self.c_col
        newrcv[2,len(rcv[2])] = 0
        self.matrix = csr_matrix((newrcv[2], (newrcv[0], newrcv[1])), shape=(self.c_row, self.c_col+1))
        
        self.c_col  = self.c_col + 1
        return True
        pass


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if(rowIndex < 0 ):
            return False
        if(rowIndex > self.c_row-1 ):
            return False
        rcv = find(self.matrix)
        newrcv = np.zeros(shape = (3, len(rcv[2]) + 1))
        for i in range(len(rcv[2])):
            if(rcv[0][i] >= rowIndex):
                newrcv[0,i] = rcv[0][i]+1                
            else:
                newrcv[0,i] = rcv[0][i]
            newrcv[1,i] = rcv[1][i]
            newrcv[2,i] = rcv[2][i]
            

        newrcv[0,len(rcv[2])] = self.c_row
        newrcv[1,len(rcv[2])] = self.c_col-1
        newrcv[2,len(rcv[2])] = 0
        self.matrix = csr_matrix((newrcv[2], (newrcv[0], newrcv[1])), shape=(self.c_row+1, self.c_col))
        
        self.c_row  = self.c_row + 1
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        if(colIndex < 0 ):
            return False
        if(colIndex > self.c_col-1 ):
            return False
        rcv = find(self.matrix)
        newrcv = np.zeros(shape = (3, len(rcv[2])+1))
        for i in range(len(rcv[2])):
            if(rcv[1][i] >= colIndex):
                newrcv[1,i] = rcv[1][i]+1                
            else:
                newrcv[1,i] = rcv[1][i]
            newrcv[0,i] = rcv[0][i]
            newrcv[2,i] = rcv[2][i]
            

        newrcv[0,len(rcv[2])] = self.c_row-1
        newrcv[1,len(rcv[2])] = self.c_col
        newrcv[2,len(rcv[2])] = 0
        self.matrix = csr_matrix((newrcv[2], (newrcv[0], newrcv[1])), shape=(self.c_row, self.c_col+1))
        
        self.c_col  = self.c_col+1
        
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        if(colIndex < 0 or colIndex >= self.c_col):
            return False
        if(rowIndex < 0 or rowIndex >= self.c_row):
            return False
        rcv = find(self.matrix)
        newrcv = np.zeros(shape = (3, len(rcv[2])+1))
        isExist = False
        for i in range(len(rcv[2])):
            newrcv[0,i] = rcv[0][i]
            newrcv[1,i] = rcv[1][i]
            newrcv[2,i] = rcv[2][i]
            if(rcv[0][i] == rowIndex and rcv[1][i] == colIndex):
                rcv[2][i] = value 
                isExist = True
        if(isExist):
            self.matrix = csr_matrix((rcv[2], (rcv[0], rcv[1])), shape=(self.c_row, self.c_col))
            return True
        else:
            newrcv[0,len(rcv[2])] = rowIndex
            newrcv[1,len(rcv[2])] = colIndex
            newrcv[2,len(rcv[2])] = value
            self.matrix = csr_matrix((newrcv[2], (newrcv[0], newrcv[1])), shape=(self.c_row, self.c_col))
            return True
        
        


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED

        return self.c_row


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return self.c_col




    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        result : [(int, int)] = []
        rcv = find(self.matrix)
        for i in range(len(rcv[2])):
            if(rcv[2][i] == value):
                result.append((rcv[0][i],rcv[1][i]))
        
        return result




    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        result : [Cell] = []
        data = self.matrix.toarray()
        for i in range(self.c_row):
            for j in range(self.c_col):
                if(data[i][j] != 0):
                    result.append(Cell(i,j,data[i][j]))
        
        return result
        
