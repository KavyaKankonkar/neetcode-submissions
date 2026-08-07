class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set()
        count=0
        first=0
        li=[]
        
        if (len(nums)<1):
            return 0
        for i in nums:
            hs.add(i)

        for n in hs:
            
            count=0
            if (n-1) not in hs:
                first=n
            while (first+count) in hs:
                count+=1
            li.append(count)

        res=max(li)

        return res