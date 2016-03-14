'''
Created on Mar 10, 2016

@author: Edielson
'''

class MergeSort(object):
    '''
    classdocs
    '''
    __Array = []
    __Sentinel=1000
    
    def __init__(self):
        '''
        Constructor
        '''
    def __Merge(self,p,q,r):
        n1 = q-p+1
        n2 = r-q
        
        L = [0 for i in range(n1+1)]
        R = [0 for i in range(n2+1)]
        
        for i in range(n1):   
            L[i]=self.__Array[(p+i-1)+1]
        for j in range(n2):   
            R[j]=self.__Array[(q+j)+1]
        
        #L[n1+1] = inf
        L[n1]=self.__Sentinel
        #R[n2+1] = inf
        R[n2]=self.__Sentinel
        
        print(L)
        print(R)
        
        i=0
        j=0
        
        for k in range(p,r+1):
            print('k=%g'%k)
            print('i=%g'%i)
            print('j=%g'%j)    
            if L[i] <= R[j]:
                self.__Array[k]=L[i]
                i=i+1
            else:
                self.__Array[k]=R[j]
                j=j+1            
    
    def __MergeSort(self,p,r): 
        if p < r:
            q=(p+r)/2
            self.__MergeSort(p,q)
            self.__MergeSort(q+1,r)
            self.__Merge(p, q, r)
    
    def Sort(self,A):
        self.__Array = A
        p=0
        r=len(A)-1
        self.__MergeSort(p, r)
        
        return self.__Array