'''
Created on Mar 10, 2016

@author: Edielson
'''

class QuickSort(object):
    '''
    classdocs
    '''
    __Array = []
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def __GetItem(self,index):
        return self.__Array[index]
    
    def __SetItem(self,index,value):
        self.__Array[index]=value
    
    def __Exchange(self,index1,index2):
        
        aux = self.__GetItem(index1)
        self.__SetItem(index1, self.__GetItem(index2))
        self.__SetItem(index2, aux)
    
    def __Partition(self,p,r):
        x = self.__GetItem(r)
        i=p-1
        #for must go from p to r-1 (inclusive), so in Python must be r
        for j in range(p, r):   
            if self.__GetItem(j) <= x:
                i=i+1
                self.__Exchange(i, j)
        self.__Exchange(i+1, r)
        return i+1
                
    
    def __QuickSort(self,p,r): 
        if p < r:
            q=self.__Partition(p,r)
            self.__QuickSort(p, q-1)
            self.__QuickSort(q+1,r)
    
    def Sort(self,A):
        self.__Array = A
        p=0
        r=len(A)-1
        self.__QuickSort(p, r)
        
        return self.__Array