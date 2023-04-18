from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


# class ListNode:
#     '''
#     Define a node in the linked list
#     '''
#
#     def __init__(self, word_frequency: WordFrequency):
#         self.word_frequency = word_frequency
#         self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------


class RowNode:
    '''
    Define a row node 
    '''

    def __init__(self, row_num = None, next = None, prev = None):
        self.row_num = row_num
        self.next = None
        self.prev = None
        self.head = None
    

class ColNode:
    '''
    Define a column node 
    '''

    def __init__(self, col_num = None, cell_data = None, next = None, prev = None):
        self.col_num = col_num
        self.cell_data = cell_data
        self.next = None
        self.prev = None

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.head = None        
        self.c_row = 0
        self.c_col = 0


    
        
    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        self.c_row = self.c_row + 1
        return True


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        self.c_col = self.c_col+1
        return True


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
        
        if(self.head == None):           
            
            self.c_row = self.c_row + 1
            return True
        else:
            temp = self.head
            isOk = False
            while(temp != None):
                if(temp.row_num >= rowIndex):
                    temp.row_num = temp.row_num + 1
                temp = temp.next
           
            self.c_row = self.c_row + 1
            return True
        


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        if(colIndex < 0 ):
            return False
        if(colIndex > self.c_col-1 ):
            return False
        
        row = self.head
        
        while(row != None):
                        
            col = row.head
            while(col != None):
                if(col.col_num >= colIndex):
                    col.col_num = col.col_num + 1
                col = col.next
            row = row.next
        self.c_col = self.c_col + 1
        return True
        


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if(colIndex < 0 or colIndex >= self.c_col):
            return False
        if(rowIndex < 0 or rowIndex >= self.c_row):
            return False
        if(self.head == None):               
            row = RowNode(rowIndex)
            row = self.insertColinRow(row, ColNode(colIndex,value))
            self.head = row
            return
        row = self.head
        prev:RowNode = None
        while(row != None):
            if(row.row_num == rowIndex):
                col = row.head
                while(col != None):
                    if(col.col_num == colIndex):
                        col.cell_data = value
                        return True
                    col = col.next
                self.insertColinRow(row, ColNode(colIndex,value))
                return True
            elif(row.row_num > rowIndex):
                temp = self.insertRowinMatrix(RowNode(rowIndex), row)
                self.insertColinRow(temp, ColNode(colIndex,value))
                return True
            prev = row
            row = row.next
        row = RowNode(rowIndex)
        self.insertColinRow(row, ColNode(colIndex,value))
        prev.next = row
        
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

        return self.c_col



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        result : [(int, int)] = []
        row = self.head
        
        while(row != None):
                        
            col = row.head
            while(col != None):
                if(col.cell_data == value):
                    result.append((row.row_num,col.col_num))
                col = col.next
            row = row.next
        return result



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        result : [Cell] = [] 
        row = self.head
        
        while(row != None):            
            col = row.head
            while(col != None):
                result.append(Cell(row.row_num, col.col_num, col.cell_data))
                col = col.next
            row = row.next
        return result
    
    def insertColinRow(self,row:RowNode, col:ColNode):
        if(row.head == None):
            row.head = col
            return row
        else:
            temp:ColNode = row.head
            prev:ColNode = None
            while(temp != None):
                if(temp.col_num > col.col_num):
                    
                    if(temp == row.head):
                        row.head = col
                        col.next = temp
                        temp.prev = col
                        return row
                        
                    else:
                        col.next = temp
                        temp.prev.next = col
                        col.prev = temp.prev
                        temp.prev = col
                        return row
                prev = temp
                temp = temp.next
            prev.next = col
            col.prev = prev
            return row
    def insertRowinMatrix(self, newrow:RowNode, indexRow:RowNode):
        if(indexRow == self.head):
            newrow.next = indexRow
            indexRow.prev = newrow
            self.head = newrow
        else:
            newrow.next = indexRow
            newrow.prev = indexRow.prev
            indexRow.prev.next = newrow
            indexRow.prev = newrow
        return newrow
    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        for cell in lCells:
            # Check If Row Node List has set  
            if (cell.row >= self.c_row):
                self.c_row = cell.row + 1
            if (cell.col >= self.c_col):
                self.c_col = cell.col + 1
            col = ColNode(cell.col, cell.val)  
            row = RowNode(cell.row) 
            isOK = False 
            if(self.head == None):               
                
                row = self.insertColinRow(row, col)
                self.head = row
                isOK = True
            else:
                temp : RowNode = self.head
                prev : RowNode = None
                while(temp != None):
                    if(temp.row_num == cell.row):
                        temp = self.insertColinRow(temp, col)
                        isOK = True
                        break
                    elif(temp.row_num > cell.row):
                        temp = self.insertRowinMatrix(row,temp)
                        
                        temp = self.insertColinRow(temp, col)
                        isOK = True
                        break
                    prev = temp
                    temp = temp.next
                if(isOK == False):
                    prev.next = row
                    row.prev = prev
                    isOK = True

                

    