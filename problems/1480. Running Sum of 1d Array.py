class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(sum(nums[:i + 1]))
        return result


assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
