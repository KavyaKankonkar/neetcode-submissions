class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)

        li=c.most_common()
        res=[]
        for i in range(len(li)):
            if li[i][1]>math.floor(len(nums)/3):
                res.append(li[i][0])

        return res