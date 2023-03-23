class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            while nums[i - 1] == nums[i]:
                nums.pop(i)
                if i >= len(nums):
                    break
            i += 1
        return len(nums)


nums = [1, 1, 2]
assert Solution().removeDuplicates(nums) == 2
assert nums == [1, 2]
