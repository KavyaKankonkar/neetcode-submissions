# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hm=defaultdict(int)
#         lt=[]
#         res=[]
#         for i in nums:
#             hm[i]+=1
        
#         for key,val in enumerate(hm) :
#             lt.append(val)
#         lt.sort()
        
#         i=len(lt)
#         while(i>0):
#             if k>0:
#                 for key,val in enumerate(hm) :
#                     if val==lt[i]:
#                         res.append(key)
#             else:
#                 return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # Create buckets where index = frequency
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Move items from map to buckets
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # Iterate backwards from highest frequency bucket
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
