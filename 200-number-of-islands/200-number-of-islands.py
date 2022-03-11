class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        lrow = len(grid)
        lcol = len(grid[0])
        
        
        def eraseIsland(grid, row, col):
            if  row<0 or row >= lrow or col<0 or col >= lcol or grid[row][col] == "0":
                return 
            
            grid[row][col] = "0"
            
            eraseIsland(grid, row+1, col)
            eraseIsland(grid, row, col+1)
            eraseIsland(grid, row-1, col)
            eraseIsland(grid, row, col-1)
        
        for row in range(lrow):
            for col in range(lcol):
                if grid[row][col] == "1":
                    count = count+1
                    eraseIsland(grid, row, col)
                    
        return count
                
                