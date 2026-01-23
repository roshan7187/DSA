class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s) :
            return []

        need = [0]*26
        window = [0]*26
        ans = []
        left = 0
        for ch in p :
            need[ord(ch) - ord('a')] += 1
        
        for ch in s[:len(p)] :
            window[ord(ch) - ord('a')] +=1

        if window == need :
            ans.append(left)

        
        for right in range(len(p),len(s)) :
            window[ord(s[right]) - ord('a')] +=1
            window[ord(s[left]) - ord('a')] -=1
            left+=1

            if window == need :
                ans.append(left)
        return ans
        