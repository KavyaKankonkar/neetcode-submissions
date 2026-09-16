import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)

        for s in strs:
            k=''.join(sorted(s))
            
            d[k].append(s)
            

        res=[]
        
        for i,v in d.items():
            res.append(v)

        return res