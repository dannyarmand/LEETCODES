from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n * (n + 1)) // 2  # Calculate the sum of all integers from 0 to n.
        actual_sum = sum(nums)  # Calculate the sum of elements in the nums array.
        missing_number = total_sum - actual_sum  # Calculate the missing number.
        return missing_number
