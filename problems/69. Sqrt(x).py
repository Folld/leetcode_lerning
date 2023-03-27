class Solution:
    def _binarySearch(self, low: int, hi: int, search: int) -> int:
        if hi - low == 1:
            return low

        mid = (low + hi) // 2
        if mid * mid > search:
            return self._binarySearch(low, mid, search)
        else:
            return self._binarySearch(mid, hi, search)

    def mySqrt(self, x: int) -> int:
        return self._binarySearch(0, x + 1, x)


assert Solution().mySqrt(8) == 2
assert Solution().mySqrt(4) == 2
assert Solution().mySqrt(1) == 1
assert Solution().mySqrt(0) == 0
assert Solution().mySqrt(2) == 1
