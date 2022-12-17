class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]


solution = Solution()
print(solution.is_palindrome(121))
