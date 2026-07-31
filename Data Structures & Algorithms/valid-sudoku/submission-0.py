class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return False
        
        for i in range(9):
            if len(board[i]) != 9:
                return False
        
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(9):
            seen_r = {}
            seen_c = {}
            for j in range(9):
                #row check
                if board[i][j] != '.':
                    if board[i][j] in seen_r or board[i][j] not in num:
                        return False
                    seen_r[board[i][j]] = True

                #column check
                if board[j][i] != '.':
                    if board[j][i] in seen_c or board[j][i] not in num:
                        return False
                    seen_c[board[j][i]] = True
        
        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                seen = {}
                for i in range(3):
                    for j in range(3):
                        val = board[row_offset + i][col_offset + j]
                        if val != '.':
                            if val in seen or val not in num:
                                return False
                            seen[val] = True

        return True