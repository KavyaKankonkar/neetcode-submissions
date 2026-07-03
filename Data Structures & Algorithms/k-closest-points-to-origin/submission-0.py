from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for i,v in enumerate(points):
            d=sqrt(points[i][0]**2 + points[i][1]**2)
            dist.append([d,v])

        dist.sort()
        res=[]
        j=0
        while(k!=0):
            res.append(dist[j][1])
            j=j+1
            k=k-1
        
        return res

        