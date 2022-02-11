class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = len(s)
        def helper(left: int, right: int):
            while left >= 0 and right < length and s[left] == s[right]:
                
                left -= 1
                right += 1

            return s[left + 1 : right]


        for index in range(len(s)):
            res = max(helper(index, index), helper(index, index+1),res, key = len) # even and odd

        return res
    
    
    
    
# def solution(str):
#   def check(str):
#     l = len(str)
#     split = l//2
#     if l%2 == 0:
#         a,b = str[:split], str[split:]
#     else:
#         a,b = str[:split], str[split+1:]
#     if a == b[::-1]:
#         return len(str)
#     else:
#         return 0
      
#   max = 1
#   ans = str[0]
#   for i in range(len(str)):
#       for j in range(len(str), i, -1):
          
#           substring = str[i:j]
#           nmax = check(substring)
#           # print(substring, i, j)
#           if nmax > max:
#               max = nmax 
#               ans = substring
#               # if j == len(str):
#               if j-i >= len(str)-(i+1):
#                 return(ans)
#   return(ans)

# import time

                