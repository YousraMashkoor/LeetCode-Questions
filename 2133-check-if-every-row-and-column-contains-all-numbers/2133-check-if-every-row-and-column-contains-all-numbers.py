class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        l = len(matrix)
        for row in matrix:
            if len(set(row)) != l:
                return False
        for col in zip(*matrix):
            if (len(set(col)) != l):
                return False
        return True
            
