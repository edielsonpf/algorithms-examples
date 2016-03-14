import time
from QuickSort import QuickSort

print('Initializes the class')
myClass = QuickSort()

A=[29, 20, 10, 15, 18, 9, 5, 13, 2, 4, 15] 

print('Applying quick sort algorithm')
start = time.clock()
NewA = myClass.Sort(A)
stop = time.clock() 
print('Done! %g seconds' %(stop-start))
print(NewA)