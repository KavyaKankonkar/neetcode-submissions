class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        op=0

        for cnt in c.values():
            if cnt==1:
                return -1
            
            op+=math.ceil((cnt+2)//3)

        return op

        
