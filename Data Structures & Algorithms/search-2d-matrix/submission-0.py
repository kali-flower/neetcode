class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) # number of rows and cols 

        top, bottom = 0, ROWS - 1 # top and bottom row 

        while top <= bottom: 
            mid_row = (top + bottom) // 2 # middle row 
            if target > matrix[mid_row][-1]: # bigger than biggest element, go greater 
                top = mid_row + 1 
            elif target < matrix[mid_row][0]: 
                bottom = mid_row - 1
            else: # target value is present in this row 
                break 

        if not (top <= bottom): 
            return False 

        row = (top + bottom) // 2 
        left, right = 0, COLS - 1

        while left <= right: 
            mid = (left + right) //2
            if target > matrix[row][mid]: 
                left = mid + 1 
            elif target < matrix[row][mid]: 
                right = mid - 1 
            else: # target found 
                return True 

        return False 