class UnionFind:
    def __init__(self, n: int):
        self.root = [num for num in range(n)]

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[y] = x

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(6)  # [0, 1, 2, 3, 4, 5]
uf.union(0, 1)  # [0, 0, 2, 3, 4, 5]
uf.union(0, 2)  # [0, 0, 0, 3, 4, 5]
uf.union(3, 5)  # [0, 0, 0, 3, 4, 3]
uf.union(5, 4)  # [0, 0, 0, 3, 5, 3]
uf.union(4, 3)  # [0, 0, 0, 3, 5, 3]
assert not uf.connected(1, 3)
uf.union(2, 4)  # [0, 0, 0, 3, 2, 3]
assert uf.connected(1, 4)
