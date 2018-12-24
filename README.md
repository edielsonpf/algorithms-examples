# sorting-algorithms
Some examples of sorting algorithms for teaching support

## Quick start

### Quicksort

```Python

import time
from QuickSort import QuickSort

print('Initializes the class')
myClass = QuickSort()

#Vector for sorting  
A=[29, 20, 10, 15, 18, 9, 5, 13, 2, 4, 15] 

print('Applying quick sort algorithm')

start = time.clock()
NewA = myClass.Sort(A)
stop = time.clock() 

print('Done! %g seconds' %(stop-start))
print(NewA)
```

### Mergesort

```Python

import time
from MergeSort import MergeSort

print('Initializes the class')
myClass = MergeSort()

#Vector for sorting 
A=[29, 20, 10, 15, 18, 9, 5, 13, 2, 4, 15] 

print('Applying merge sort algorithm')

start = time.clock()
NewA = myClass.Sort(A)
stop = time.clock() 

print('Done! %g seconds' %(stop-start))
print(NewA)
```

### Heapsort

```Python

import time
from HeapSort import HeapSort 

print('Initializes the class')
myHeap = HeapSort()

#Vector for sorting 
A=[29, 20, 10, 15, 18, 9, 5, 13, 2, 4, 15] 

print('Applying heap sort algorithm')

start = time.clock()
NewA = myHeap.Sort(A)
stop = time.clock() 

print('Done! %g seconds' %(stop-start))
print(NewA)
```
