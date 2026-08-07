class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        
        for i in range(len(s)):
            if ('A'<=s[i]<='Z' or
            'a'<=s[i]<='z' or
            '0'<=s[i]<='9'):
                
               res+=s[i].lower()
        
        new="".join(reversed(res))

        for i in range(len(res)):
            if (new[i]!=res[i]):
                return False
        
        return True
        