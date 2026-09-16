class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       c=Counter(nums)
       li=[]
    
       res=c.most_common(k)
       for n in res:
        li.append(n[0])
       
       return li
