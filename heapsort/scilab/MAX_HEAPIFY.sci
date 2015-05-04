function A = MAX_HEAPIFY(A,i,heap_size)
    l=2*i;
    r=2*i+1;
    if((l<=heap_size) & (A(l)>A(i)))
        maior=l;
    else 
        maior=i;
    end
    if((r<=heap_size) & (A(r)>A(maior)))
        maior=r;
    end
    if (maior~=i) then
        aux = A(i);
        A(i)=A(maior);
        A(maior)=aux;
        A = MAX_HEAPIFY(A,maior);
    end
endfunction
