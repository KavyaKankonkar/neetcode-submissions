class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l=0
        r=k-1
        freq=Counter(blocks[l:r+1])
        replace=float("inf")

        while r<len(blocks):
            replace=min(k-freq["B"],replace)
            freq[blocks[l]]-=1
            l+=1
            r+=1
            if r<len(blocks):
                freq[blocks[r]]+=1

        return int(replace)
            