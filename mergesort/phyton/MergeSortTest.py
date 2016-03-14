import time
from MergeSort import MergeSort

print('Initializes the class')
myClass = MergeSort()

A=[29, 20, 10, 15, 18, 9, 5, 13, 2, 4, 15] 

print('Applying merge sort algorithm')
start = time.clock()
NewA = myClass.Sort(A)
stop = time.clock() 
print('Done! %g seconds' %(stop-start))
print(NewA)