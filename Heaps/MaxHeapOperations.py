class MaxHeap:
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
        """ Return's a string repr. of the heap """

        return ' '.join([str(val) for val in self.arr[1:]])

    def leftChild(self, idx):
        """ Returns left child index. """
        return (2*idx)

    def rightChild(self, idx):
        """ Returns left child index. """
        return (2*idx + 1)

    def maxHeapify(self, idx):
        """ Heapify the current subtree """

        l = self.leftChild(idx)
        r = self.rightChild(idx)
        largest = idx

        if l < self.heapSize and self.arr[idx] < self.arr[l]:
            largest = l
        if r < self.heapSize and self.arr[largest] < self.arr[r]:
            largest = r
        if largest != idx:
            self.arr[idx], self.arr[largest] = self.arr[largest], self.arr[idx]
            self.maxHeapify(largest)

    def buildHeap(self):
        """ Builds max heap """

        for i in range(self.heapSize//2, 0, -1):
            self.maxHeapify(i)
    
    def heapCheck(self, idx):
        """ 
        - Checks the heap 
        :Parem idx: index of the parent
        :return: Trueness of the current sub-tree
        """

        l = self.leftChild(idx)
        r = self.rightChild(idx)
        largest = idx
        if l < self.heapSize and self.arr[idx] < self.arr[l]:
            largest = l

        if r < self.heapSize and self.arr[idx] < self.arr[r]:
            largest = r

        if largest == i:
            return True
        return False
    
    def getMax(self):
        """ The max of the heap """
        
        if len(self.arr) < 2:
            return 'The heap is empty'
        else:
            return self.arr[1]

    def extractMax(self):
        """ Extracts the max element of the Heap """

        if len(self.arr) < 2:
            return "The Heap is empty"
        else:
            ret_val = self.arr[1]
            self.arr[1] = self.heapSize[-1]
            self.heapSize -= 1
            return ret_val

def main():
    """ The main function """

    size = int(input())
    arr = list(map(int,input().split()))
    obj = MaxHeap(size, arr)
    obj.buildHeap()
    print(obj)


if __name__ == '__main__':
    main()