from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


class RowNode:
    '''
    Define a row node 
    '''

    def __init__(self, row_num = None, next = None, prev = None):
        self.row_num = row_num
        self.next = next
        self.prev = prev
        self.head = None
    

class ColNode:
    '''
    Define a column node 
    '''

    def __init__(self, col_num = None, cell_data = None, next = None, prev = None):
        self.col_num = col_num
        self.cell_data = cell_data
        self.next = next
        self.prev = prev

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.head = None        
        self.c_row = 0
        self.c_col = 0

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        for cell in lCells:
            # Check If Row Node List has set  
            if (cell.row >= self.c_row):
                self.c_row = cell.row
            if (cell.col >= self.c_col):
                self.c_col = cell.col
            if(self.head == None):
                col = ColNode(cell.col, cell.val)
                row = RowNode(cell.row,col)
                row.head = col
                self.head = row
                print("insert")
                print(row.next)
                print(col.next)
            else:
                
                row = self.head
                isOk = False
                while(row.next != None):
                    if(row.row_num == cell.row):
                        
                        col = row.head
                        
                        while(col.next != None):
                            if(col.col_num > cell.col):
                                newcol = ColNode(cell.col, cell.val)
                                if(col == row.head):
                                    row.head = newcol
                                    newcol.next = col
                                    col.prev = newcol
                                    isOk = True
                                    break
                            
                            col = col.next
                        if(isOK == False):
                            newcol = ColNode(cell.col, cell.val)
                            col.next = newcol
                            newcol.prev = col
                            isOK = True
                            break
                        
                    elif(row.row_num > cell.row):
                        col = ColNode(cell.col, cell.val)
                        newrow = RowNode(cell.row,col)
                        newrow.head = col
                        if(row == self.head):
                           newrow.next = row
                           row.prev = newrow
                           self.head = newrow
                           isOK = True
                           break
                        else:
                           row.prev.next = newrow
                           newrow.prev = row.prev
                           newrow.next = row
                           row.prev = newrow
                           isOK = True
                           break
                    row = row.next
                if(isOK == False):
                    if(row != self.head):
                        col = ColNode(cell.col, cell.val)
                        newrow = RowNode(cell.row,col)
                        row.next = newrow
                        newrow.prev = row
                        
                        isOK = True
                    

            # if self.col_node_list.head == None:
            #     self.col_node_list.head = new_col_node
            # else:
            #     while self.col_node_list is not None:
            #         if self.row_node_list.current == 

    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.
        @return True if operation was successful, or False if not.
        """

        # new_row_node = RowNode(self.c_row)
        # self.row_node_list.tail = new_row_node
        # self.c_row += 1

        return True


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        
        # new_col_node = ColNode(self.c_col)
        # self.col_node_list.tail = new_col_node
        # self.c_col += 1

        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        # TO BE IMPLEMENTED
        pass

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
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
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

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        # TO BE IMPLEMENTED
        result : [Cell] = [] 
        row = self.head
        print(row.row_num)
        print(row.next)
        while(row != None):
            print("pp")
            print(row)
            col = row.head
            while(col != None):
                result.append(Cell(row.row_num, col.col_num, col.cell_data))
                col = col.next
            row = row.next
        return result
