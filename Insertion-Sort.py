// string to sort
myA = [5,2,4,6,1,3]

// Insertion Sort function
def InsertionSort (A):
    // Loop of the List/Array and start index 1
    for j, elem in enumerate(A[1:], start=1):
        key = elem
        i = j-1
        // compare the current element with its predecessor until
        // we reach the beginning of the array (i.e. current elememt
        // is the smallest or the next predecessor is smaller than our element
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        // copy the current elem to the position                                                
        A[i+1] = key

print 'before' + str(myA)
InsertionSort(myA)
print 'after' + str(myA)
