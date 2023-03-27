class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"


assert Solution().addBinary("11", "1") == "100"
assert Solution().addBinary("1010", "1011") == "10101"
