class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
       #*************** Simple Pythonic way
        
        # s[:] = s[::-1]
        
        
        # ************* Problem solving approah
        
        x = []
        for i in range(len(s)-1, -1, -1):
            x.append(s[i])
        s[:] = x[:]