class Solution:
    def maxArea(self, height: List[int]) -> int:
        # using brute force approach
        
        def getArea(start, end):
            return min(height[start], height[end]) * (end - start)

        start = 0
        end = len(height)-1
        area = 0
        
        while start<end:
            area = max(area, getArea(start,end))
            if height[start] < height[end]:
                start += 1
                while height[start] < min(height[start], height[end]):
                    strat +=1
            else:
                end -= 1
                while height[end] < min(height[start], height[end]):
                    end -=1
        return area