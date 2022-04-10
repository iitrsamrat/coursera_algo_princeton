import numpy as np

class ElementrySort:
    def __init__(self):
        pass

    def __swap__(self, ar, i, j):
        temp = ar[j]
        ar[j] = ar[i]
        ar[i] = temp

    def selection_sort(self, ar):
        n = len(ar)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                if ar[j] < ar[min_idx]:
                    min_idx = j

            if min_idx != i:
                self.__swap__(ar, i, min_idx)

        return ar

    def bubble_sort(self, ar):
        n = len(ar)
        for i in range(n-1):
            for j in range(i+1, n):
                if ar[i] > ar[j]:
                    self.__swap__(ar, i, j)
        return ar


if __name__ == '__main__':
    for i in range(10):
        ar = np.random.randint(-10, 100, 100)
        print("input          : {}".format(ar))
        es = ElementrySort()
        print("output of ssort: {}".format(es.selection_sort(ar)))
        print("output of bsort: {}".format(es.bubble_sort(ar)))
        print("\n")







