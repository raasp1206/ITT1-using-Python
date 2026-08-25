class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                col -= 1
            else:
                row += 1
        return False
