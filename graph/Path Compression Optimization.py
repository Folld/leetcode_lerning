# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(7)  # [0, 1, 2, 3, 4, 5]
uf.union(0, 2)  # [0, 0, 0, 3, 4, 5]
uf.union(0, 1)  # [0, 0, 2, 3, 4, 5]
uf.union(3, 5)  # [0, 0, 0, 3, 4, 3]
uf.union(5, 4)  # [0, 0, 0, 3, 5, 3]
uf.union(4, 3)  # [0, 0, 0, 3, 5, 3]
assert not uf.connected(1, 3)
uf.union(2, 4)  # [0, 0, 0, 3, 2, 3]
assert uf.connected(1, 4)
