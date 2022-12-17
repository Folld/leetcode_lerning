from collections import Counter


class Solution:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def halves_are_alike(self, s: str) -> bool:
        mid = len(s) // 2
        left, right = s[:mid], s[mid:]
        left_vow = self.find_vowels(left)
        right_vow = self.find_vowels(right)
        return left_vow == right_vow

    def find_vowels(self, s: str) -> int:
        counter = Counter(s)
        result = 0
        for letter, value in counter.items():
            if letter in self.vowels:
                result += value
        return result


word = "AbCdEfGh"
solution = Solution()
print(solution.halves_are_alike(word))

