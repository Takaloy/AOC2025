class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n  # each set starts with size 1

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
            self.size[rootA] += self.size[rootB]

        return True

    def set_size(self, x: int) -> int:
        return self.size[self.find(x)]
