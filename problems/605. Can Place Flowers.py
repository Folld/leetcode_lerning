class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        result = 0
        previous = 0
        for flow in flowerbed:
            if previous == 0 and flow == 0:
                result += 1
                flow = 1
            if previous and flow:
                result -= 1
            previous = flow

        return result >= n


assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
assert Solution().canPlaceFlowers([1, 0, 0, 0, 2], 2) is False
