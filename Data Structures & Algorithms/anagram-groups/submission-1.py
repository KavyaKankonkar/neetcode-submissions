class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        res=[]
        for s in strs:
            st="".join(sorted(s))
            hm[st].append(s)

        for li in hm.values():
            res.append(li)

        return res

