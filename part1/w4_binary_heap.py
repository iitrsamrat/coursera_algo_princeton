# https://www.coursera.org/learn/algorithms-part1/lecture binary-heaps
import random
import time

class BinaryHeap:
    def __init__(self):
        self.pq = list()

    def sink(self, idx):

        n = self.size()

        while 2 * idx + 1 < n:
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            max_idx = left_child
            if right_child < n:
                if self.less(left_child,right_child):
                    max_idx = right_child
            else:
                if not self.less(idx, left_child):
                    break

            self.exch(idx, max_idx)
            idx = max_idx

    def swim(self, idx):
        while idx > 0:
            pidx = (idx - 1) // 2
            #print(pidx, idx)
            if self.less(pidx, idx):
                # assume its left
                self.exch(pidx, idx)
                idx = pidx
            else:
                break

    def exch(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    # is index i val less than j
    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def size(self):
        return len(self.pq)

    def is_empty(self):
        return self.size() == 0

    def insert(self, val):
        self.pq.append(val)
        # swim up to max position val for max Binary Heap
        self.swim(self.size()-1)


    def del_max(self):
        if self.size() == 0:
            raise Exception("EMPTYPQ")
        # max is always at the root
        temp = self.pq[0]
        self.pq[0] = self.pq[self.size()-1]
        self.pq.pop()
        self.sink(0)
        return temp



if __name__ == "__main__":
    upq = BinaryHeap()
    for i in range(100):
        ran_i = random.randint(1, 100)
        time.sleep(1)
        if ran_i < 80:
            print("After insert {}".format(ran_i))
            upq.insert(ran_i)
            print(upq.pq)
        else:
            try:
                print("delete max should be = {} and is = {}".format(max(upq.pq), upq.del_max()))
                print(upq.pq)
            except Exception as e:
                print(e)

