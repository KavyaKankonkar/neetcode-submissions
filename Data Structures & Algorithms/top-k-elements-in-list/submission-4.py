class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)
       
        res=[]
    
        r=hm.most_common(k)
        j=0
        while(k!=0):
            res.append(r[j][0])
            j+=1
            k-=1

        return res