class Solution:

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        left_cursor = right_cursor = 0
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] < right[right_cursor]:
                result.append(left[left_cursor])
                left_cursor += 1
            else:
                result.append(right[right_cursor])
                right_cursor += 1
        result.extend(left[left_cursor:])
        result.extend(right[right_cursor:])
        return result

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_list = self._merge(nums1, nums2)
        mid = len(merged_list) // 2
        if len(merged_list) % 2 == 0:
            return float((merged_list[mid] + merged_list[mid - 1]) / 2)
        return float(merged_list[mid])


s = Solution()

assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
