class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    mask = 1 << (int(board[r][c]) - 1)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def get_choices(r: int, c: int) -> int:
            return ~(rows[r] | cols[c] | boxes[(r // 3) * 3 + (c // 3)]) & 0x1FF

        def backtrack() -> bool:
            min_choices = 10
            best_r, best_c, best_mask = -1, -1, 0
            
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        choices = get_choices(r, c)
                        count = bin(choices).count('1')
                        if count == 0:
                            return False
                        if count < min_choices:
                            min_choices = count
                            best_r, best_c, best_mask = r, c, choices
                            if min_choices == 1:
                                break
                if min_choices == 1:
                    break
                    
            if min_choices == 10:
                return True
                
            r, c = best_r, best_c
            b = (r // 3) * 3 + (c // 3)
            
            while best_mask:
                lsb = best_mask & -best_mask
                best_mask ^= lsb
                val = lsb.bit_length()
                
                board[r][c] = str(val)
                rows[r] |= lsb
                cols[c] |= lsb
                boxes[b] |= lsb
                
                if backtrack():
                    return True
                    
                board[r][c] = '.'
                rows[r] ^= lsb
                cols[c] ^= lsb
                boxes[b] ^= lsb
                
            return False

        backtrack()

       