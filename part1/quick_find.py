class QuickFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.n = n

    def isConnected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        if pid == qid:
            return
        for i in range(self.n):
            if self.id[i] == pid:
                self.id[i] = qid

if __name__ == '__main__':
    qf = QuickFind(10)
    qf.union(3, 4)
    print(qf.id)
    qf.union(3, 8)
    print(qf.id)
    qf.union(6, 5)
    print(qf.id)
    qf.union(9, 4)
    print(qf.id)
    qf.union(2, 1)
    print(qf.id)

    print("is connected {} {} = {}".format(8, 9, qf.isConnected(9, 8)))
    print("is connected {} {} = {}".format(5, 0, qf.isConnected(5, 0)))
    print("is connected {} {} = {}".format(7, 2, qf.isConnected(7, 2)))
    qf.union(5, 0)
    print(qf.id)
    print("is connected {} {} = {}".format(5, 0, qf.isConnected(5, 0)))
    qf.union(7, 2)
    qf.union(6, 1)

    print("is connected {} {} = {}".format(1, 0, qf.isConnected(1, 0)))
    print(qf.id)