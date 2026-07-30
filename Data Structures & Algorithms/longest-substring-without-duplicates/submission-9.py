class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        
        for i in range(len(s)):
            hs=set()
            for j in range(i,len(s)):
                if s[j] in hs:
                    break
                hs.add(s[j])
            res=max(res,len(hs))
        return res