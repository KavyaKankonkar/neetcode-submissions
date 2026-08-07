class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closeness={}
        res=[]
        li=[]
        for num in arr:
            res.append((abs(x-num),num))
        res.sort()
        for i in range(k):
            li.append(res[i][1])
        li.sort()
        return  li


