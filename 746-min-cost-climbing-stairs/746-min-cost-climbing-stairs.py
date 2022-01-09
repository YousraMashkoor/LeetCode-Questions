'''
** Google Interview Question

ref: https://www.youtube.com/watch?v=ktmzAZWkEZ0
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         i = len(cost)
#         c = 0
#         while i > 1: #  [10,15,20]
#             minimum = min(cost[i-1], cost[i-2])
#             i = (i-2 if cost[i-2]==minimum else i-1)
#             c += minimum
#         return c
            

        cost.append(0)
        for i in range(len(cost)-3, -1 , -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])
            
            