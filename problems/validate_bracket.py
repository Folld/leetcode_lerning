class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in hash_map:
                stack.append(char)
            elif not stack or char != hash_map.get(stack.pop()):
                return False
        return not stack



assert Solution().isValid("{()}") is True
assert Solution().isValid("()") is True
assert Solution().isValid("()[]{}") is True
assert Solution().isValid("{()}") is True
assert Solution().isValid("") is True
assert Solution().isValid("[") is False
assert Solution().isValid("]") is False
