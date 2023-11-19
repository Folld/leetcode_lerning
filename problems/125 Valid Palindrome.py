import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        prepared_str = re.sub(r'[\W_]', '', s).lower()
        return prepared_str[::-1] == prepared_str


s = Solution()

assert s.isPalindrome('ab_a') is True
assert s.isPalindrome('A man, a plan, a canal: Panama') is True
assert s.isPalindrome('A man, a plan, a anal: Panama') is True
assert s.isPalindrome('My mother is Dart Aider') is False
