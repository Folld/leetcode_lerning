import heapq


class Solution:
    """
    Given the array of integers nums, you will choose two different indices i and j of that array.
    Return the maximum value of (nums[i]-1)*(nums[j]-1).
    """

    def maxProduct(self, nums: list[int]) -> int:
        m, prev_m = heapq.nlargest(2, nums)
        return (m - 1) * (prev_m - 1)


if __name__ == '__main__':
    s = Solution()

    assert s.maxProduct([3, 4, 5, 2]) == 12
    assert s.maxProduct([1, 5, 4, 5]) == 16
    assert s.maxProduct([3, 7]) == 12
