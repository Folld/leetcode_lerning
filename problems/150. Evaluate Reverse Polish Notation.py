class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(token)
            else:
                x, y = stack.pop(), stack.pop()
                stack.append(int(eval(f'{y} {token} {x}')))
        return stack.pop()


solution = Solution()

assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert solution.evalRPN(["1"]) == 1
