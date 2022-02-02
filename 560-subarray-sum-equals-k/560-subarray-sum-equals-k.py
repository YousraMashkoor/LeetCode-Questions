## Commulative Sum 
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        seen = collections.Counter({0:1})
        sum = 0
        count = 0
        
        for _, x in enumerate(nums):
            sum += x
            count += seen[sum-k]
            seen[sum] +=1 
        return count
        