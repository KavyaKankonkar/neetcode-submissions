class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=len(s1)
        
        for i in range(len(s2)):
            if sorted(s2[i:i+l])==sorted(s1):
                return True
        return False

