class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        res=""
        l=min(l1,l2)
        i=0
        while(l!=0):
            res+=word1[i]
            res+=word2[i]
            l-=1
            i+=1

        if l1!=l2:
           if l1>l2:
               res+=word1[i:]
           elif l2>l1:
                res+=word2[i:]
        
        return res
            