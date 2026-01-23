class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s) :
            return []

        need = Counter(p)
        window = Counter(s[:len(p)])
        ans = []
        left = 0

        if window == need :
            ans.append(left)

        
        for right in range(len(p),len(s)) :
            window[s[right]] +=1
            window[s[left]] -=1

            if window[s[left]] == 0 :
                del window[s[left]]
            left+=1

            if window == need :
                ans.append(left)
        return ans
        