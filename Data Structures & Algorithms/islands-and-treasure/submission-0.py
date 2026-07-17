class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()

        rows=len(grid)
        cols=len(grid[0])

        visited={}
        def dfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or grid[r][c]==-1:
                return
            v=grid[r][c]+1
            visited[(r,c)]=1
            for dr,dc in [[0,1],[0,-1],[-1,0],[1,0]]:
                new_r=r+dr
                new_c=c+dc
                if new_r<0 or new_r==rows or new_c<0 or new_c==cols or grid[new_r][new_c]==-1:
                    continue
                if grid[new_r][new_c]!=0:
                    if grid[new_r][new_c] >v:
                        grid[new_r][new_c]=v 
                        visited[(new_r,new_c)]=1   
                        dfs(new_r,new_c)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    dfs(r,c)

        

            
