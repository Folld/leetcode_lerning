# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x: int) -> int:
        """
        tc: O(1)
        """
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        """
        tc: O(n)
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x

    def connected(self, x: int, y: int) -> bool:
        """
        tc: O(1)
        """
        return self.root[x] == self.root[y]


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
assert uf.connected(1, 5)
assert uf.connected(5, 7)
assert not uf.connected(4, 9)
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
assert uf.connected(4, 9)
