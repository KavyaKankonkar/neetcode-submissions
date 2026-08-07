class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        st1=sorted(s1)
        st2=sorted(s2)
        l=len(s1)
        n=len(s2)

        for i in range(n):
            s=s2[i:i+l]
            s=sorted(s)
            if s == st1:
                return True
        
        return False

            


        