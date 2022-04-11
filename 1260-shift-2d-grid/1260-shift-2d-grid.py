class Solution:
    
    def shiftGrid(self, grid, k):
        
        k = k % (len(grid) * len(grid[0]))
        
        linear = []
        for level in grid :
            linear.extend(level)
        
        linear = linear[-k:] + linear[:-k]
        l = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = linear[l]
                l += 1
        
        return grid
    
#     def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         print(grid)
        
#         m = len(grid)
#         n = len(grid[0])
#         r, c = 0
#         first = grid[r][c]
        
#         for r in range(m):
#             for c in range(n):
            
#                 grid[r][c+1] = grid[r][c]
            
            
#             if c%3 == 0:
#                 grid[r][c+1] = grid[]
            
        