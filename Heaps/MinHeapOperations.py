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

    def __str__(self):
        """ Returns the string repr. """

        rep = ''
        for node in (self.arr[1:]):
            rep += str(node)
            rep += ' '
        
        return rep

    def leftChild(self, idx):
        """ Returns left child index. """
        return (2*idx)

    def rightChild(self, idx):
        """ Returns left child index. """
        return (2*idx + 1)

    def minHeapify(self, idx):
        """ Heapify the current subtree """

        l = self.leftChild(idx)
        r = self.rightChild(idx)
        smallest = idx

        if l < self.heapSize and self.arr[idx] > self.arr[l]:
            smallest = l
        if r < self.heapSize and self.arr[smallest] > self.arr[r]:
            smallest = r
        if smallest != idx:
            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            self.minHeapify(smallest)

    def buildHeap(self):
        """ Builds min heap """

        for i in range(self.heapSize//2, 0, -1):
            self.minHeapify(i)
    
    def heapCheck(self, idx):
        """ 
        - Checks the heap 
        :Parem idx: index of the parent
        :return: Trueness of the current sub-tree
        """

        l = self.leftChild(idx)
        r = self.rightChild(idx)
        smallest = idx
        if l < self.heapSize and self.arr[idx] > self.arr[l]:
            smallest = l

        if r < self.heapSize and self.arr[idx] > self.arr[r]:
            smallest = r

        if smallest == i:
            return True
        return False

    def getmin(self):
        if len(self.arr) >= 2:
            return self.arr[1]
        else:
            print('No elements in the heap')

    def extractMin(self):
        if len(self.arr) >= 2:
            ele = self.arr[1]
            self.arr[1] = self.arr[self.heapSize]
            self.heapSize -= 1
        else:
            print('Insufficent Elements')

def main():
    """ The main function """

    size = int(input())
    arr = list(map(int,input().split()))
    obj = MinHeap(size, arr)
    obj.buildHeap()
    print(obj)


if __name__ == '__main__':
    main()