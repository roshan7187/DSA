class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        str =""
        
        for ch in s :
            if '0' <= ch <='9' or 'a' <= ch <= 'z' :
                str+=ch
        n = len(str)
        for ind in range(0,n//2):
            if str[ind] != str[-ind-1] :

                return False
        return True
