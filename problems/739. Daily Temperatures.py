from random import randrange


class Solution:
    @staticmethod
    def daily_temperatures(temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top_stack_index = stack.pop()[-1]
                count = index - top_stack_index
                result[top_stack_index] = count
            stack.append((temp, index))
        return result


sol = Solution()
nums = [randrange(30, 100) for _ in range(10_000_000)]
print(sol.daily_temperatures(nums))
