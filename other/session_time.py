from collections import defaultdict


class Solution:
    @staticmethod
    def get_longest_session(*sessions: tuple[int, int]) -> int:
        counter: dict[int, int] = defaultdict(int)
        for session in sessions:
            start_time, end_time = session
            for i in range(start_time, end_time + 1):
                counter[i] += 1
        return max(counter.items(), key=lambda x: x[-1])[0]


s = Solution()
assert s.get_longest_session(
    (3, 4),
    (1, 6),
    (0, 7),
) == 3
