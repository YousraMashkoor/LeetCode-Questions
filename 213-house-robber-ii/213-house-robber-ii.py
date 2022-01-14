class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):

            rob1, rob2 = 0, 0

            # [rob1, rob2, n, n+1, ...]
            for n in nums:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))