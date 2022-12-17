class Solution:
    def sort_array(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        left_list = self.sort_array(nums[0:pivot])
        right_list = self.sort_array(nums[pivot:])
        return self.merge(left_list, right_list)

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
print(s.sort_array(numbers))
numbers.sort()
