class Solution:

    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(string) ->bool :
            l,r=0,len(string)-1
            while l<r:
                if string[l]!=string[r] :
                    return False
                l+=1
                r-=1
            return True

        if isPalindrome(s):
            return True

        for i in range(len(s)):
            new_string=s[:i]+s[i+1:]
            if isPalindrome(new_string):
                return True

        return False

     