class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        sp='€'
        for i in strs:
            res+=i
            res+=sp
        return res

    def decode(self, s: str) -> List[str]:
        strs=[]
        lt=''
        sp='€'
        for i in range(len(s)):
            if s[i]!=sp:
                lt+=s[i]
            else:
                strs.append(lt)
                lt=''
        return strs

