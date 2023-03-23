class Solution:
    n: int

    def totalNQueens(self, n: int) -> int:
        self.n = n
        return self.backtrack(0, set(), set(), set())

    def backtrack(self, row, cols, diags, antidiags):
        if row == self.n:
            return 1

        count = 0
        for col in range(self.n):
            if col not in cols and row - col not in diags and row + col not in antidiags:
                cols.add(col)
                diags.add(row - col)
                antidiags.add(row + col)
                count += self.backtrack(row + 1, cols, diags, antidiags)
                cols.remove(col)
                diags.remove(row - col)
                antidiags.remove(row + col)
        return count


assert Solution().totalNQueens(4) == 2
assert Solution().totalNQueens(1) == 1
assert Solution().totalNQueens(5) == 10
assert Solution().totalNQueens(6) == 4
