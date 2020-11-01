class MinHeap:
    """ Array implmention of Heap """

    # Initilize the values.
    def __init__(self, n, arr):
        """
        :param n: Size of the array.
        :param arr: The given array.
        :return: None
        """

        self.heapSize = n + 1
        self.arr = [0] + arr

    def leftChild(self, idx):
        """ Returns left child index. """
        return (2*idx)

    def rightChild(self, idx):
        """ Returns left child index. """
        return (2*idx + 1)

    def minHeapify(self, idx):
        """ Heapify the current subtree """

        print('cycle here')
        l = self.leftChild(idx)
        r = self.rightChild(idx)
        print('index = ', idx)
        print('left index = ', l)
        print('right index = ', r)
        print(self.arr[idx])
        print(self.arr)
        print([i for i in range(len(self.arr))])
        smallest = idx

        if l < self.heapSize and self.arr[idx] > self.arr[l]:
            print(self.arr[l])
            smallest = l
        if r < self.heapSize and self.arr[smallest] > self.arr[r]:
            print(self.arr[r])
            smallest = r
        if smallest != idx:
            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            print(self.arr)
            print([i for i in range(len(self.arr))])
            self.minHeapify(smallest)
        print('-'*100)

    def buildHeap(self):
        """ Builds min heap """

        for i in range(self.heapSize//2, 0, -1):
            self.minHeapify(i)

def main():
    size = int(input())
    arr = list(map(int,input().split()))
    obj = MinHeap(size, arr)

    obj.buildHeap()
    print(obj.arr)


if __name__ == '__main__':
    main()