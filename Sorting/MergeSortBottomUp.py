"""
Merge Sort - Bottom Up Approach

Time Complexity:
O(n logn) - We split the list in half each time. It will take approximately logn splits
to get down to single elements which are therefore sorted. Then the merge operation is linear
as we have to iterate through all the elements in the two lists we are merging. And we do the
merge operation the number of times we split so the total running time is O(nlogn).

Space Complexity:
O(n) - Merge sort is not done in place so we need to allocate memory for storing the sorted output.

Considerations:
A list can have 0 or 1 elements.
A list can have an even or odd number of elements.
The list may already be sorted.
A list may contain duplicate elements.

Applications:
Merge sort is often the best choice for sorting a linked list.
Merge sort is good for types of lists where the data can only be efficiently accessed sequentially.
Can be used in external sorting.

Notes:
Merge sort is a stable sorting algorithm
Merge sort is a divide and conquer algorithm.

"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
  
        mergeSort(L)
        mergeSort(R)

        merge(L, R, arr)

def merge(L, R, arr):
  
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
  
if __name__ == '__main__':
    arr = [0, -1, 11, 17, 5, 6, -5]
    print("starting array: ", arr)
    mergeSort(arr)
    print("sorted array: ", arr)
