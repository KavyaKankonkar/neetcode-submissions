class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        
        def capture(r,c):
            if r<0 or r==rows or c<0 or c==cols or board[r][c]=="X" or board[r][c]=="T":
                return 
            board[r][c]="T"
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                capture(r+dr,c+dc)


        for r in range(rows):
            for c in range(cols):
                if r==0 or r==rows-1:
                    if board[r][c]=="O":
                        capture(r,c)
                else:
                    if c==0 or c==cols-1:
                        if board[r][c]=="O":
                            capture(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"
                
            
        

        

        

