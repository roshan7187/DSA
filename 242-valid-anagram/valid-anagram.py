class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for ch in s:
                if s.count(ch) != t.count(ch):
                    return False
                    break
            return True
        return False