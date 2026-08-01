class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=len(s1)
        s=sorted(s1)
        for i in range(len(s2)):
            if sorted(s2[i:i+l])==s:
                return True
        return False

