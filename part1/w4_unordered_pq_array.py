import random
class UnorderedPQ:
    def __init__(self):
        self.pq = list()

    def  size(self):
        return len(self.pq)

    def is_empty(self):
        return len(self.pq) == 0

    def insert(self, val):
        self.pq.append(val)
        return self

    def del_max(self):
        max = 0
        n = self.size()
        for i in range(n):
            if self.pq[i] > self.pq[max]:
                max = i

        if max == n:
            return self.pq.pop(n-1)
        else:
            temp = self.pq[n-1]
            self.pq[n-1] = self.pq[max]
            self.pq[max] = temp
            return self.pq.pop(n-1)


if __name__ == "__main__":
    upq = UnorderedPQ()
    for i in range(10):
        upq.insert(random.randint(1, 10))
    print(upq.pq)
    for i in range(10):
        print(upq.del_max())