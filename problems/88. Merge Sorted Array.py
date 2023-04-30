class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y = 0, 0
        nums1[:], nums2[:] = nums1[:m], nums2[:n]
        while x < len(nums1) and y < len(nums2):
            if nums1[x] >= nums2[y]:
                nums1.insert(x, nums2[y])
                y += 1
            x += 1
        nums1.extend(nums2[y:])


def test_case1():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s = Solution()
    s.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]
    assert len(nums1) == 6


def test_case2():
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    s = Solution()
    s.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]
    assert len(nums1) == 6


test_case2()
test_case1()
