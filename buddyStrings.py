class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Check if the lengths of the strings are different
        if len(s) != len(goal):
            return False  # If the lengths are different, it's not possible to swap characters

        # Check if s and goal are identical
        if s == goal:
            # Check if there are duplicate characters in s
            # If there are, swapping two occurrences of the same character will result in equal strings
            # Return True if there are duplicates, False otherwise
            return len(set(s)) < len(s)

        # Find the indices where s and goal differ
        indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indices.append(i)

        # Check if there are exactly two indices that differ
        if len(indices) != 2:
            return False  # If there are more or fewer than two differing indices, it's not possible to swap characters

        # Check if swapping the characters at the differing indices results in equal strings
        i, j = indices[0], indices[1]
        return s[i] == goal[j] and s[j] == goal[i]


solution = Solution()
result = solution.buddyStrings("ab", "ba")
print(result)  # Output: True
result = solution.buddyStrings("ab", "ab")
print(result)  # Output: FALSE
result = solution.buddyStrings("aa", "aa")
print(result)  # Output: True
