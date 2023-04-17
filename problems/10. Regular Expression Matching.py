import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p, s))


s = Solution()
assert s.isMatch('aa', 'a') is False
assert s.isMatch('aa', 'a*') is True
assert s.isMatch('aa', '.*') is True
