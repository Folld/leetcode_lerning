class Solution:
    def sort_array(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sort_array(nums[:mid])
        right = self.sort_array(nums[mid:])
        return self.merge(left, right)

    @staticmethod
    def merge(left_list: list, right_list: list) -> list:
        left_cursor = right_cursor = 0
        result = []
        while (left_cursor < len(left_list)) and (right_cursor < len(right_list)):
            if left_list[left_cursor] < right_list[right_cursor]:
                result.append(left_list[left_cursor])
                left_cursor += 1
            else:
                result.append(right_list[right_cursor])
                right_cursor += 1
        result.extend(left_list[left_cursor:])
        result.extend(right_list[right_cursor:])
        return result


numbers = [5, 2, 3, 1]
s = Solution()
assert s.sort_array(numbers) == [1, 2, 3, 5]
