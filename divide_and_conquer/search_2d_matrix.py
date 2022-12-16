class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            result = self.binary_search(row, target)
            if result:
                return result
        return False

    def binary_search(self, row: list[int], target: int):
        low = 0
        middle = len(row) // 2
        top = len(row)
        if row[middle] == target:
            return True
        if len(row) <= 1:
            return
        if row[middle] > target:
            top = middle
        elif row[middle] < target:
            low = middle
        return self.binary_search(row[low:top], target)


if __name__ == '__main__':
    m = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    s = Solution()
    print(s.search_matrix(m, 5))
