class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hr=defaultdict(list)
        hc=defaultdict(list)
        hs=defaultdict(list)
        rows=len(board)
        cols=len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==".":
                    continue
                if board[r][c] in hr[r] or board[r][c] in hc[c] or board[r][c] in hs[(r//3,c//3)]:
                    return False
                hr[r].append(board[r][c])
                hc[c].append(board[r][c])
                hs[(r//3,c//3)].append(board[r][c])

        return True

