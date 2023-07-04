class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        str_x = str(x)

        # Compare the string with its reverse
        return str_x == str_x[::-1]
# Create an instance of the Solution class
sol = Solution()

# Check if a number is a palindrome
print(sol.isPalindrome(121))  # True
print(sol.isPalindrome(123))  # False
