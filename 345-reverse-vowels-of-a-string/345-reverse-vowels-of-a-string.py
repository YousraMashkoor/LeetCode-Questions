class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        back = len(s)-1
        for char in range(len(s)-1):
            if back <= char:
                break
            if s[char] in ['u', 'a', 'e', 'i', 'o', 'A', 'E', 'I', 'O', 'U']:
                while(s[back] not in ['u', 'a', 'e', 'i', 'o', 'A', 'E', 'I', 'O', 'U']):
                    back -= 1
                s[char], s[back] = s[back], s[char]
                back -= 1
        return "".join(s)
                    