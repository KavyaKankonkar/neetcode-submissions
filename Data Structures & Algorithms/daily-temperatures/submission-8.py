class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if stk == []:
                stk.append((temperatures[i],i))
            else:
                if stk[-1][0]>temperatures[i]:
                    res[i]=stk[-1][1]-i
                    stk.append((temperatures[i],i))
                else:
                    while stk!=[] and temperatures[i]>=stk[-1][0] :
                        stk.pop()
                    if stk !=[]:
                        res[i]=stk[-1][1]-i
                        stk.append((temperatures[i],i))
                    else:
                        res[i]=0
                        stk.append((temperatures[i],i))
        return res
        


        