import heapq


class Solution:
    """
    You are given an m x n matrix grid consisting of positive integers.

    Perform the following operation until grid becomes empty:

    Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
    Add the maximum of deleted elements to the answer.
    Note that the number of columns decreases by one after each operation.

    Return the answer after performing the operations described above.
    """

    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        result = 0
        grid = [[-1 * n for n in row] for row in grid]
        while grid:
            tmp = 0
            for i, row in enumerate(grid):
                if not row:
                    grid.pop(i)
                    continue
                heapq.heapify(row)
                tmp = max(-heapq.heappop(row), tmp)
            result += tmp
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]) == 8
    assert s.deleteGreatestValue([[10]]) == 10
    assert s.deleteGreatestValue([[58, 42, 8, 75, 28], [35, 21, 13, 21, 72]]) == 216
