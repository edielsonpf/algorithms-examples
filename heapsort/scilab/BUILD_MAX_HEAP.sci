function [A]=BUILD_MAX_HEAP(A,n)
    heap_size=n;
    for i=n/2:-1:1
 	  A=MAX_HEAPIFY(A,i,heap_size);
    end
endfunction

