import time
from HeapSort import HeapSort 

print('Initializes the class')
myHeap = HeapSort()

print('Applying heap sort algorithm')
A=[29, 20, 10, 15, 18, 9, 5, 13, 2, 4, 15] 
start = time.clock()
NewA = myHeap.Sort(A)
stop = time.clock() 
print('Done! %g seconds' %(stop-start))
print(NewA)