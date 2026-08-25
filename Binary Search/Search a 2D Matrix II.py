class Solution:
    def searchMatrix(self, matrix, target):
        # Handle empty matrix edge case safely
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)
        n = len(matrix[0])
        
        # Start at the top-right corner element
        row = 0
        col = n - 1
        
        while row < m and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                # Target is smaller; eliminate this entire column
                col -= 1
            else:
                # Target is larger; eliminate this entire row
                row += 1
                
        return False
