class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)
        li=hm.most_common(k)
        res=[]
        for n in li:
            res.append(n[0])
        
        return res