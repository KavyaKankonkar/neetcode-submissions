class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap={0:0}

        for g in wall:
            total=0
            for b in g[:-1]:
                total+=b
                countGap[total]=countGap.get(total,0)+1
            
        return len(wall)-max(countGap.values())