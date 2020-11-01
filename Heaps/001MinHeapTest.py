from BuildMinHeap import MinHeap
from random import randint

# 1. Create Heaps.
# 2. Check each Heap.
# 3. Run this whole code.

def create_heap():
    """ creates heap for testing """

    no_tst = randint(100, 1000)
    heap_lst = []
    for i in range(no_tst):
        size = randint(0, 1000)
        arr = []
        for i in range(size):
            ele = randint(0, 100000000)
            arr.append(ele)
        obj = MinHeap(size, arr)
        obj.buildHeap()
        heap_lst.append(obj)
    
    return heap_lst


def check_min_heap(test_cases):
    """ Checks for a min heap """

    result = [False for i in range(len(test_cases))]
    for idx, obj in enumerate(test_cases):
        for i in range(1, obj.heapSize):
            if obj.heapCheck == False:
                result[idx] = False
                break
        else:
            result[idx] = True

    return result


def final_check(result):
    """ Displays the final result """
    
    ret_val = True
    for flag in result:
        if flag == False:
            return False
    return True


def main():
    """ The main function """

    test_cases = create_heap()
    result = check_min_heap(test_cases)
    pass_res = final_check(result)
    if final_check:
        print('This passes the test cases.')
    else:
        print('The code does not work properly')

if __name__ == '__main__':
    main()