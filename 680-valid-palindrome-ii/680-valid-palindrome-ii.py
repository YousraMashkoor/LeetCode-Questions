class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def diffChar(a, b):
            """
            returns the 2 indexes of missmatched char from palimdrome
            """
            for i,c in enumerate(a):
                if b[i] != a[i]:
                    return i, len(a)-1-i
        
        def isPalindrome(s):            
            if s == s[::-1]:
                return True
            else:
                return False
            
            
        if isPalindrome(s):
            return True
        else:
            i1, i2 = diffChar(s,s[::-1])
            if isPalindrome(s[:i1]+s[i1+1:]):
                return True
            else:
                return isPalindrome(s[:i2]+s[i2+1:])
