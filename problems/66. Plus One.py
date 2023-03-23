class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = int(''.join([str(d) for d in digits])) + 1
        return [int(d) for d in str(result)]


assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
assert Solution().plusOne([8, 9]) == [9, 0]
