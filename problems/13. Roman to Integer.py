class Solution:
    _roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def roman_to_int(self, s: str) -> int:
        result = 0
        for i in range(len(s)-1, -1, -1):
            num = self._roman_map[s[i]]
            if 3 * num < result:
                result = result - num
            else:
                result = result + num
        return result


sol = Solution()
print(sol.roman_to_int('MCMXCI'))


