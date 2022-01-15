class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            if len(set(row)) != len(matrix):
                return False
        for col in zip(*matrix):
            if (len(set(col)) != len(matrix)):
                return False
        return True
            
