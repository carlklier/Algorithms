"""
Merge Sort - Bottom Up Approach

Time Complexity:
O(n logn) - We split the list in half each time. It will take approximately logn splits
to get down to single elements which are therefore sorted. Then the merge operation is linear
as we have to iterate through all the elements in the two lists we are merging. And we do the
merge operation the number of times we split so the total running time is O(nlogn).

O(nlogn) on average as well.

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
Merge sort is a comparison sort requiring a total ordering

"""

def mergeSort(arr):
 
    low = 0
    high = len(arr) - 1
 
    # copy the initial array
    temp = arr[:]
 

    # blocks of size m
    m = 1
    while m < len(arr):
 
        for i in range(low, high, 2*m):
            start = i
            mid = i + m - 1
            end = min(i + 2*m - 1, high)
            merge(arr, temp, start, mid, end)
 
        m = 2*m

def merge(arr, temp, start, mid, end):
  
    i = start
    j = mid + 1
    k = start

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

# the second half items will already be in the right spot

  # copy the updates back to original array
    for i in range(start, end + 1):
      arr[i] = temp[i]

  
if __name__ == '__main__':
    arr = [0, -1, 11, 17, 5, 6, -5]
    print("starting array: ", arr)
    mergeSort(arr)
    print("sorted array: ", arr)
