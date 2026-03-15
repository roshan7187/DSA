class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        ans = 0
        while left < len(s)-2:
            if s[left] != s[left+1] != s[left+2] and s[left] != s[left+2]:
                ans+=1
                left+=1
            else:
                left+=1
        return ans