class Solution:
    def count_and_print_repeating(self, a: str):
        char_count = {}  # Dictionary to store the count of each character

        for c in a:  # Iterate over each character in the string
            if c in char_count:
                char_count[c] += 1  # If the character already exists in the dictionary, increment its count
            else:
                char_count[c] = 1  # If the character is encountered for the first time, set its count to 1

        most_repeated_char = ''  # Variable to store the most repeated character found
        max_count = 0  # Variable to store the maximum count of any character

        for c, count in char_count.items():  # Iterate over the dictionary items (character, count)
            if count > max_count:  # If the current count is greater than the previous maximum count
                max_count = count  # Update the maximum count
                most_repeated_char = c  # Update the most repeated character

        return most_repeated_char

    def find_most_repeated(self, a: str) -> str:
        char_count = {}  # Dictionary to store the count of each character

        for c in a:  # Iterate over each character in the string
            if c in char_count:
                char_count[c] += 1  # If the character already exists in the dictionary, increment its count
            else:
                char_count[c] = 1  # If the character is encountered for the first time, set its count to 1

        for c, count in char_count.items():  # Iterate over the dictionary items (character, count)
            print(f"Character '{c}' appears {count} times")

        return self.count_and_print_repeating(a)  # Call the count_and_print_repeating method to find the most repeated character

sol = Solution()

sol.count_and_print_repeating('abcdea')

most_repeated = sol.find_most_repeated('abcdssssssssssssssssea')
print("Most repeated character:", most_repeated)
