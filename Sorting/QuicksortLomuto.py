"""
Quicksort - Lomuto partition scheme

TODO: Confirm when the worst case time complexity occurs

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


Notes:
Quicksort is a comparison sort requiring a total ordering
Quicksort is a divide and conquer algorithm.
Quicksort is NOT a stable sort.
The Lomuto partition scheme chooses the last element as the pivot element
The lomuto partition scheme is less efficient than Hoare's scheme when all the elements are equal.
The worst case time complexity for the Lomuto partition scheme occurs when the elements
 are already sorted or all the elements
are the same.

"""

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]
    
  i = i+1
  arr[i], arr[high] = arr[high], arr[i]
  return i

def quicksortLomuto(arr, low, high):
  if low >= high:
    return
  
  p = partition(arr, low, high)
  quicksortLomuto(arr, low, p - 1)
  quicksortLomuto(arr, p + 1, high)
  
if __name__ == '__main__':
    arr = [0, -1, 11, 17, 5, 6, -5]
    print("starting array: ", arr)
    quicksortLomuto(arr, 0, len(arr) - 1)
    print("sorted array: ", arr)
