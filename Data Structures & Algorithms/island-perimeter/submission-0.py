class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid_copy=deepcopy(grid)

        rows=len(grid)
        cols=len(grid[0])
        perim=0
        for i in range(rows):
            for j in range(cols):
                v=4
                if grid_copy[i][j] ==1:
                    for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                        new_i= i+dx
                        new_j= j+dy         
                        if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                            continue
                        if grid_copy[new_i][new_j] ==1 :
                            v-=1
                    perim+=v
        return perim

