class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        grid_c=deepcopy(grid)
        max_area=0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid_c[r][c]==0:
                return 0
            
            grid_c[r][c]=0
            area=1
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                area+=dfs(r+dr,c+dc)
            return area

        for r in range(rows):
            for c in range(cols):
                max_area=max(max_area,dfs(r,c))
        
        return max_area
