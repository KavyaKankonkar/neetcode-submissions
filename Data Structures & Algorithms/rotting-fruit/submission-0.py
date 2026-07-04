class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        grid_copy=deepcopy(grid)

        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        fresh_count=0
        
        for i in range(rows):
            for j in range(cols):
                if grid_copy[i][j]==2 :
                    queue.append((i,j))
                if grid_copy[i][j]==1 :
                    fresh_count+=1
        mins=0
        while len(queue)!=0 and fresh_count>0 :
            mins+=1
            totalrot=len(queue)
            for _ in range(totalrot):
                i,j=queue.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i = i+dx 
                    new_j = j+dy
                    if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                        continue
                    if grid_copy[new_i][new_j]==0 or grid_copy[new_i][new_j]==2 :
                        continue
                    fresh_count-=1
                    grid_copy[new_i][new_j]=2
                    queue.append((new_i,new_j))
        if fresh_count > 0:
            return -1
        return mins

