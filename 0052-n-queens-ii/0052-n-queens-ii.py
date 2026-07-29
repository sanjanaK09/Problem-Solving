class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        def backtrack(row, cols, diags1, diags2):
            if row == n:
                self.count += 1
                return
                
            available_slots = ((1 << n) - 1) & ~(cols | diags1 | diags2)
            
            while available_slots:
                position = available_slots & -available_slots
                available_slots ^= position
                
                backtrack(
                    row + 1, 
                    cols | position, 
                    (diags1 | position) << 1, 
                    (diags2 | position) >> 1
                )
                
        backtrack(0, 0, 0, 0)
        return self.count
        