class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        n=0
        grid_c=deepcopy(grid)

        def dfs(r,c):
            if (r>=rows or r<0 or c>=cols or c<0 or grid_c[r][c]=="0"):
                    return
                

            grid_c[r][c]="0"
            for dr,dc in [[0,1],[0,-1],[-1,0],[1,0]]:
                new_i=r+dr
                new_j=c+dc
                dfs(new_i,new_j)
                
                            
        for i in range(rows):
            for j in range(cols):
                if grid_c[i][j]=="1":
                    dfs(i,j)
                    n+=1

        
        return n

                
