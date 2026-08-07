class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list[str])
        for i in strs:
            s="".join(sorted(i))
            hm[s].append(i)

        res=[]

        for n in hm.values():
            res.append(n)

        return res