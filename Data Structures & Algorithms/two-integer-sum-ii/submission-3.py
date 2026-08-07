class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hs={}
        res=[]
        for i in range(len(numbers)):
            hs[i+1]=numbers[i]

        
        for i in range(len(numbers)):           
            if (target-numbers[i]) in hs.values():
                for j,n in hs.items():
                    if (n==target-numbers[i]):
                        res.append(i+1)
                        res.append(j)
                        return res
        
                
                