class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hm={}
        for ch in s:
            hm[ch]=hm.get(ch,0)+1

        for ch in t:
            if ch not in hm or hm[ch]==0:
                return False
            hm[ch]-=1
        return True



