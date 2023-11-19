import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-val for val in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            if (diff := -1 * heapq.heappop(heap) + heapq.heappop(heap)):
                heapq.heappush(heap, -diff)
        return 0 if not heap else (-1 * heap[0])


if __name__ == '__main__':
    s = Solution()
    assert s.lastStoneWeight([1]) == 1
    assert s.lastStoneWeight([1, 2]) == 1
    assert s.lastStoneWeight([3, 1]) == 2
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([1, 2, 3, 4, 5, 100]) == 85
    assert s.lastStoneWeight([1, 2, 3, 100, 4, 5]) == 85
    assert s.lastStoneWeight([9, 3, 2, 10]) == 0
