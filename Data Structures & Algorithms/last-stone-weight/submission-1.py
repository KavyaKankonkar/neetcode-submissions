class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sl=len(stones)
        if not stones:
            return 0
        if sl==1:
            return stones[0]
        
        stones.sort()

        y=stones.pop()
        x=stones.pop()

        if x<y:
          stones.append(y-x)  
        
        return self.lastStoneWeight(stones)