class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        hm=defaultdict(int)
        curr_len=0
        while r!=len(s):
            while s[r] in hm and hm[s[r]]>=1 and l<r:
                hm[s[l]]-=1
                l+=1

            hm[s[r]]+=1

            curr_len=max(curr_len,r-l+1)
            r+=1
        return curr_len