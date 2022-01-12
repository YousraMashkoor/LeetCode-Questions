import re
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        idx = 0
        substr = ""
        while idx < len(s):
            substr += s[idx]
            if len(set(substr)) == len(substr):
                max_len = max(max_len, len(substr))
            else:
                substr = substr[substr.find(s[idx])+1:]
            idx += 1            
        return max_len
        