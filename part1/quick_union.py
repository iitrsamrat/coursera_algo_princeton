class QuickUnion:
    def __init__(self, n):
        self.n = n
        self.id = [i for i in range(self.n)]

    def __root(self, p):
        ppid = self.id[p]
        while ppid != self.id[ppid]:
            ppid = self.id[ppid]
        return ppid

    def isConnected(self, p, q):
        ppid = self.__root(p)
        pqid = self.__root(q)
        return ppid == pqid

    def union(self, p, q):
        # O(N) search too tall tree
        ppid = self.__root(p)
        pqid = self.__root(q)
        # O(1) union
        self.id[ppid] = pqid
        return self

if __name__ == '__main__':
    qu = QuickUnion(10)
    qu.union(4, 3).union(3, 8).union(6,5).union(9,4).union(2,1).union(9, 8)
    print(qu.id)

    print("is connected {} {} = {}".format(8, 9, qu.isConnected(9, 8)))
    print("is connected {} {} = {}".format(0, 1, qu.isConnected(0, 1)))

    qu.union(5, 0)
    print(qu.id)
    print("is connected {} {} = {}".format(0, 6, qu.isConnected(0, 6)))

