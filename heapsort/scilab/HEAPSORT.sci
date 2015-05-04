function A=HEAPSORT(A,n)
    heap_size=n;
    A=BUILD_MAX_HEAP(A,n);
    disp("MAX HEAP:");
    disp(A);
    for i=n:-1:2
        aux=A(1);
        A(1)=A(i);
        A(i)=aux;
        heap_size=heap_size-1;
        A=MAX_HEAPIFY(A,1,heap_size);
        disp(i);
        disp(A);
    end
endfunction
