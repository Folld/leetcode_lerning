class Solution:
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result.extend(matrix.pop(0))

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            if matrix:
                result.extend(matrix.pop()[::-1])

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop(0))

        return result


s = Solution()
assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert s.spiralOrder([[7], [9], [6]]) == [7, 9, 6]
assert s.spiralOrder([[1]]) == [1]
