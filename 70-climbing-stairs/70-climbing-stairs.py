'''
** Amazon Interview Question **

#### Solution:

 > solved using a binary tree
    > bcz after every step there's 2 ways to take another step (1 or 2)
 
 > Can use DFS (depth first search)
    > time complexity would be 2^n
    
#### Dynamic Programming Solution:

 1. more better solution would be memoization
    > time complexity would be O(n)


 2. But this can se solved using the true DP approach called ** DP Bottom Up **
    > use an array
    > solve the base case (last step: for example for n=5)
        > so if we're on step 5 there's only "1" way to reach there bcz you're already there
    > then step before it (second last step for n=5)
        > so if we're on step 4 there's only "1" way to reach there
    > ans for last and second last step would always be 1 we we'll use these value to start
    > then step before BEFORE it (thisrd last step)
        > this would be the sum of last 2 steps (in this case "1" + "1")
    > and so on
    
ref: https://www.youtube.com/watch?v=Y0lT9Fck7qI

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        
        for x in range(n-1):
            temp = one
            one = one + two
            two = temp
            
        return one