#BINARY SEARCH

def binary_search(arr, target):
    low = 0  # Initialize the lower index to the first element
    high = len(arr) - 1  # Initialize the higher index to the last element

    while low <= high:  # Repeat the following steps until the search space is empty
        mid = (low + high) // 2  # Calculate the middle index by dividing the sum of low and high by 2

        if arr[mid] == target:  # If the middle element is equal to the target, we found it!
            return mid
        elif arr[mid] < target:  # If the middle element is smaller than the target, search in the right half
            low = mid + 1  # Update the lower index to be the element to the right of the middle
        else:  # If the middle element is greater than the target, search in the left half
            high = mid - 1  # Update the higher index to be the element to the left of the middle

    return -1  # If the target is not found, return -1 to indicate it's not present

# Usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = binary_search(arr, target)
print("Found at index:", result)
#BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)  # Get the number of elements in the array

    for i in range(n):  # Repeat the following steps for each element in the array
        for j in range(n - 1):  # Compare adjacent elements from the beginning to the second-to-last element
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next one
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements to bring the smaller one forward

# Usage:
arr = [5, 2, 8, 1, 9, 3]
bubble_sort(arr)
print("Sorted array:", arr)

#FACTORIAL

def factorial(n):
    if n == 0 or n == 1:  # Base case: If n is 0 or 1, return 1 since the factorial of 0 and 1 is 1
        return 1

    result = 1
    for i in range(2, n + 1):  # Multiply numbers from 2 to n to get the factorial
        result *= i

    return result

# Usage:
num = 5
fact = factorial(num)
print("Factorial of", num, "is", fact)

#FIBONNACII

def fibonacci(n):
    if n <= 1:  # Base case: If n is 0 or 1, return n as they are the first two Fibonacci numbers
        return n

    a, b = 0, 1  # Initialize variables for the first two Fibonacci numbers

    for _ in range(2, n + 1):  # Start from the third Fibonacci number up to the desired position (n)
        a, b = b, a + b  # Calculate the next Fibonacci number by summing the previous two

    return b  # Return the Fibonacci number at position n

# Usage:
num = 10
fib = fibonacci(num)
print("Fibonacci number at position", num, "is", fib)

You got it, partner! Here's a short explanation of each algorithm in plain text, tailored for a newbie like yourself:

Binary Search Algorithm:

Imagine you have a sorted list of values, and you want to find a particular value.
Binary search is like a guessing game. You start by looking at the middle value of the list.
If the value you're looking for is equal to the middle value, great! You found it!
If the value is less than the middle value, you know it must be in the lower half of the list.
If the value is greater, it must be in the upper half of the list.
You keep narrowing down the search space by repeatedly dividing the list in half until you find the value or determine it's not there.
Binary search is efficient because it eliminates half of the remaining possibilities with each comparison.
Bubble Sort Algorithm:

Imagine you have a group of cowpokes lined up in random order, and you want to arrange 'em in order by their hat sizes.
Bubble sort works by repeatedly comparing adjacent cowpokes and swapping 'em if they're in the wrong order.
In each pass, the largest hat size "bubbles" up to the end of the line.
This process is repeated until the whole line is sorted.
Bubble sort may not be the most efficient sorting algorithm, but it's simple to understand and implement.
Factorial Algorithm:

Imagine you have a bunch of cows, and you want to know how many different ways you can line 'em up in a straight line.
The factorial algorithm helps you with that. You start with a number and multiply it by all the smaller numbers down to 1.
For example, if you have 5 cows, the factorial is calculated as 5 * 4 * 3 * 2 * 1, which equals 120.
The result gives you the total number of possible arrangements.
Factorial is used in many mathematical and combinatorial calculations.
Fibonacci Sequence Algorithm:

Imagine a pair of rabbits in a field, and each month they produce a new pair of rabbits.
The Fibonacci sequence gives you the numbers that represent how many rabbits there are after each month.
The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
So, the sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, and so on.
Fibonacci numbers have interesting mathematical properties and can be found in various natural phenomena.

