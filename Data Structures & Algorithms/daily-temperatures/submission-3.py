class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackT=stack[-1][0]
                stackInd=stack[-1][1]
                res[stackInd]=i-stackInd
                stack.pop()
            stack.append((t,i))

        return res
