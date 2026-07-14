class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd={}
        for i,c in enumerate(order):
            orderInd[c]=i
        
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]

            for j in range(len(w1)):
                if j==len(w2):
                    return False
                
                ind1=w1[j]
                ind2=w2[j]
                if w1[j]!=w2[j]:
                    if orderInd[ind1] >orderInd[ind2]:
                        return False
                    break
        return True