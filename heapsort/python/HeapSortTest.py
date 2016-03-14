import time
from HeapSort import MaxHeap 

A=[29, 20, 10, 15, 18, 9, 5, 13, 2, 4, 15] 
print('Initializes the class')
myHeap = MaxHeap(A)
print('The array is internally transformed in a max heap')
print(myHeap.GetHeap())

print('Applying heap sort algorithm')
start = time.clock()
NewA = myHeap.Sort()
stop = time.clock() 
print('Done! %g seconds' %(stop-start))
print(NewA)
