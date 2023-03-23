class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high, = 0, len(nums)
        while low < high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return high


assert Solution().searchInsert([1, 3, 4, 5, 6], 5) == 3
assert Solution().searchInsert([1, 3, 5, 6], 4) == 2
assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
assert Solution().searchInsert([1, 3, 5, 6], 0) == 0
assert Solution().searchInsert([1, 3, 5, 6, 8], 4) == 2
assert Solution().searchInsert([1, 3, 5, 6, 8], 8) == 4
