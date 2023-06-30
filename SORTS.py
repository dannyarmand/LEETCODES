def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]  # Select the element to be inserted
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements greater than key to the right
            j -= 1
        
        arr[j + 1] = key  # Insert the key at the correct position

# Usage:
arr = [5, 2, 8, 1, 9, 3]
insertion_sort(arr)
print("Sorted array:", arr)


def radix_sort(arr):
    # Find the maximum element to determine the number of digits
    max_val = max(arr)
    digit_count = len(str(max_val))

    for d in range(digit_count):
        # Create 10 buckets (0-9) for each digit position
        buckets = [[] for _ in range(10)]

        # Distribute elements into the buckets based on the current digit
        for num in arr:
            digit = (num // 10**d) % 10
            buckets[digit].append(num)

        # Concatenate elements from all buckets in order
        arr = [num for bucket in buckets for num in bucket]

    return arr

# Usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quicksort(left) + middle + quicksort(right)  # Recursively sort the subarrays and combine them

# Usage:
arr = [5, 2, 8, 1, 9, 3]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]  # Split the array into two halves
    right = arr[mid:]

    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)  # Merge the sorted halves

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Usage:
arr = [5, 2, 8, 1, 9, 3]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than the current root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the current root
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap the root with the largest child

        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heapsort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum) element with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

# Usage:
arr = [5, 2, 8, 1, 9, 3]
heapsort(arr)
print("Sorted array:", arr)
Insertion Sort:

Imagine you have a deck of cards, and you want to sort them in ascending order.
Insertion sort works by dividing the deck into two parts: sorted and unsorted.
It iterates through the unsorted part, comparing each card to the cards in the sorted part and inserting it in the correct position.
At each iteration, the algorithm picks a card from the unsorted part and places it in its proper position in the sorted part.
Insertion sort is straightforward to implement but can be slow for large lists.
Radix Sort:

Radix sort is a non-comparative sorting algorithm that sorts elements based on their individual digits or characters.
It sorts the elements by processing them digit by digit, starting from the least significant digit to the most significant digit.
The algorithm uses a bucket-based approach, distributing elements into different buckets based on each digit's value.
By repeatedly distributing and collecting elements based on each digit, radix sort eventually sorts the entire list.
Radix sort is particularly useful for sorting numbers or strings with fixed-length representations.
QuickSort:

QuickSort is a divide-and-conquer algorithm that sorts elements by selecting a "pivot" and partitioning the list into two sublists: elements less than the pivot and elements greater than the pivot.
The algorithm then recursively sorts the two sublists.
QuickSort is known for its efficiency and average-case performance.
However, in the worst-case scenario where the pivot selection is poor, QuickSort can have a high time complexity, making it less efficient than other sorting algorithms.
MergeSort:

MergeSort is another divide-and-conquer algorithm that divides the list into smaller sublists until each sublist contains a single element.
It then merges the sublists back together, sorting them in the process.
The merging step compares the elements from the two sublists and places them in order.
MergeSort guarantees a time complexity of O(n log n) and is known for its stable sorting property.
It performs well on large lists but requires additional space for the merging process.
HeapSort:

HeapSort utilizes the concept of a binary heap, which is a complete binary tree that satisfies the heap property (parent nodes are either greater or smaller than their children).
The algorithm builds a max-heap or min-heap from the input list, depending on whether it wants to sort in ascending or descending order.
Once the heap is constructed, HeapSort repeatedly extracts the maximum (or minimum) element from the heap, swaps it with the last element in the list, and then restores the heap property.
HeapSort has a time complexity of O(n log n) and sorts the list in place without requiring additional memory.
