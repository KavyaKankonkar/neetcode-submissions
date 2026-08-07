class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s)!=len(t)):
            return False
        hs=set()
        su=sorted(s)
        tu=sorted(t)
        for i in range(len(t)):
            if su[i]!=tu[i]:
                return False
        
        return True


