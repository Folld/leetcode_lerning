class Solution:
    def reverse(self, x: int) -> int:
        value = int(str(abs(x))[::-1])
        if x < 0:
            value = -1 * value
        if value < -2 ** 31 or value > 2 ** 31 - 1:
            return 0
        return value


s = Solution()

assert s.reverse(1534236469) == 0
assert s.reverse(-123) == -321
assert s.reverse(123) == 321
assert s.reverse(120) == 21
