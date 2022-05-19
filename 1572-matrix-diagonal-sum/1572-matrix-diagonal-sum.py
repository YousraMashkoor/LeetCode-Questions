class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum = 0
        col = len(mat)-1
        for row in range(len(mat)):
            sum += mat[row][row]
            if (row != col):
                sum += mat[row][col]
            col -=1
        return sum
            