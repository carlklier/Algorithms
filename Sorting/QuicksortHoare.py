"""
Quicksort - Hoare partition scheme

TODO: Confirm when the worst case time complexity occurs
TODO: Understand why we include the pivot element in the recursive call

Time Complexity:
O(n^2) - In the worst case, each partition will contain 1 less element than the previous
paritition, requiring n-1 nested calls before reaching a list size of 1. And each nested call
takes linear time to process.
The worst case occurs when all the elements are equal or when the list is already sorted.

O(nlogn) on average

Space Complexity:
O(1) - Quicksort can be done in place.
O(logn) space required if counting stack space and using Sedgewick's optimizations.
Else, O(n) space required for stack space.

Considerations:
A list can have 0 or 1 elements.
A list can have an even or odd number of elements.
The list may already be sorted.
A list may contain duplicate elements.

Applications:
A good approach when merge sort isn't as applicable.
A better/faster approach than Lomuto's partition scheme because it does 3 times fewer
swaps on average.


Notes:
Quicksort is a comparison sort requiring a total ordering
Quicksort is a divide and conquer algorithm.
Quicksort is NOT a stable sort.
The Hoare partition scheme chooses the middle element as the pivot element
The worst case time complexity for the hoare partition scheme occurs when the
 pivot is chosen as the largest or smallest
element repeatedly.

"""

def partition(arr, low, high):
  pivot = arr[(low + high)//2]
  i = low - 1
  j = high + 1
  
  while True:
    i+=1
    while arr[i] < pivot:
      i+=1

    j-=1  
    while arr[j] > pivot:
      j-=1

    if i>=j:
      return j
    
    arr[i], arr[j] = arr[j], arr[i]

def quicksortHoare(arr, low, high):
  if low >= high:
    return
  
  p = partition(arr, low, high)
  quicksortHoare(arr, low, p) # we include the pivot here
  quicksortHoare(arr, p + 1, high)
  
if __name__ == '__main__':
    # arr = [0, -1, 11, 17, 5, 6, -5]
    arr = [1, 1, 1, 1, 1]
    print("starting array: ", arr)
    quicksortHoare(arr, 0, len(arr) - 1)
    print("sorted array: ", arr)
