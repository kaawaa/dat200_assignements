#  *** PYTHON IMPLEMENTATION ***
def insertionSort(arr):
  # Start from 1 as arr[0] is always sorted
  for i in range(1, len(arr)): 
    currentElement = arr[i]
    # Move elements of arr[0..i-1], that are greater than key, 
    # to one position ahead of their current position
    j = i-1
    print("a")
    while j >= 0 and arr[j] > currentElement :
        arr[j + 1] = arr[j]
        j -= 1
     # Finally place the Current element at its correct position.
    arr[j + 1] = currentElement
    print(arr)
# Driver code to test above
arr = [-20, -16, 8, -3, 9, 14, 1, -8, -17, 5]
insertionSort(arr)