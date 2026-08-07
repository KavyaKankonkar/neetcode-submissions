class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)

        lt=[]
        res=[]
        n=0
        for w,i in hm.items():
            
            res=hm.most_common(k)
            while(k!=0):
                lt.append(res[n][0])
                n+=1
                k-=1

        lt.sort()
        
        return lt

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         # Create buckets where index = frequency
#         freq = [[] for i in range(len(nums) + 1)]

#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
        
#         # Move items from map to buckets
#         for n, c in count.items():
#             freq[c].append(n)

#         res = []
#         # Iterate backwards from highest frequency bucket
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
