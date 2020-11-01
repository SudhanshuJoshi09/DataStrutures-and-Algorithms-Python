# Heaps
- ## Applications of Heaps
  1. HeapSort
  2. Priority Queues
  3. Graph Algorithms: Prims, Dijkstra's
  4. K'th largest element in a array.
  5. Sort a almost sorted Array.
  6. Merger K sorted Arrays.
  

- ## Binary Heaps
  - MinHeap Operations
       - getmin() - O(1) Time
       - extractmin() - O(logn) Time
       - decreasekey() - O(logn) Time
       - insert() - O(logn) Time
       - delete() - O(logn) Time
       <br/>
  - MaxHeap Operations
       - getmax() - O(1) Time
       - extractmax() - O(logn) Time
       - increasekey() - O(logn) Time
       - insert() - O(logn) Time
       - delete() - O(logn) Time
       <br />
  - **How is Binary Heap represented?**
  <br />
    > A Binary Heap is a Complete Binary Tree. A binary heap is typically
    > represented as an array.
    
     The root element will be at Arr[0].
     Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:
     Arr[(i-1)/2]	Returns the parent node
     Arr[(2*i)+1]	Returns the left child node
     Arr[(2*i)+2]	Returns the right child node