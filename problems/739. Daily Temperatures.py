class Solution:
    @staticmethod
    def daily_temperatures(temperatures: list[int]) -> list[int]:
        result = [0 for _ in temperatures]
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top_idx = stack.pop()[-1]
                count = idx - top_idx
                result[top_idx] = count
            stack.append((temp, idx))
        return result


sol = Solution()
nums = [30, 45, 31, 46, 25, 60, 90, 32, 33, 31, 30, 30, 100]
assert sol.daily_temperatures(nums) == [1, 2, 1, 2, 1, 1, 6, 1, 4, 3, 2, 1, 0]
