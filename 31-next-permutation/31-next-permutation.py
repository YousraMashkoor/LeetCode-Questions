class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # To find next permutations, we'll start from the end
        i = j = len(nums)-1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return 
        if i == 0:
            nums.reverse()
            return 
        # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        while nums[j] <= nums[i-1]:
            j -= 1
        # Now out pointer is pointing at two different positions
        # i. first non-assending number from end
        # j. first number greater than nums[i-1]
        
        # We'll swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # We'll reverse a sequence strating from i to end
        nums[i:]= nums[len(nums)-1:i-1:-1]
        # We don't need to return anything as we've modified nums in-place
        
#         def updatePeak(nums, i):
#             p = i
#             c = i-1
            
#             if c < 0:
#                 return p
#             for idx, x in enumerate(nums[i+1:]):
#                 if x < nums[p] and x > nums[c]:
#                     p = idx
#             return p
        
#         def findPeak(nums):
#             i = nums[::-1].index(max(nums))
#             i = len(nums)-(i+1)
#             print("find peak",nums[i])
#             return updatePeak(nums, i)
        
        
#         if len(nums)==1:
#             return
        
#         i = findPeak(nums)
#         print(i, nums[i])
        
        
        