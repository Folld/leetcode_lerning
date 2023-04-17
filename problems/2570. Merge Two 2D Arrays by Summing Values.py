from collections import defaultdict


class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result = defaultdict(int)
        for i, val in nums2:
            result[i] += val
        for i, val in nums1:
            result[i] += val
        return sorted([list(item) for item in result.items()])


s = Solution()

assert s.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]) == [[1, 6], [2, 3], [3, 2], [4, 6]]
assert s.mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
