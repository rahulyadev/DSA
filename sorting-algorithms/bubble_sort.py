def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Initialize a flag that will help to detect if any swap is made
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped, the list is sorted
        if not swapped:
            break
    return arr