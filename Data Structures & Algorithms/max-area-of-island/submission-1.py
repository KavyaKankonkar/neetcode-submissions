class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        grid_c=deepcopy(grid)

        max_area=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def area(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid_c[r][c]==0:
                return 0
            
            grid_c[r][c]=0
            
            return (1 + area(r,c+1)+area(r,c-1)+area(r+1,c)+ area(r-1,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid_c[r][c]==1 :
                    max_area=max(area(r,c),max_area)                    
        return max_area

            
            
