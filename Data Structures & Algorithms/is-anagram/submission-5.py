class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted=sorted(s)
        t_sorted=sorted(t)
        if len(s)!=len(t):
            return False
        else:
            j=0
            for i in range(0,len(s)):
                   if (s_sorted[i]!=t_sorted[j]):
                    return False
                   else:
                        j=i+1
                 
            return True

                