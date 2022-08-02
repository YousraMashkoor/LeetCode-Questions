class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        while low < high:
            mid = low + (high - low) // 2
            if sum(bisect.bisect(row, mid) for row in matrix) < k:   # how many numbers are on the left of middle number
                low = mid + 1
            else:
                high = mid
        return low