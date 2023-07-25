class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []  # List to store all valid IP addresses
        self.recurse(s, ans, 0, "", 0)  # Start the recursive process
        return ans  # Return the list of valid IP addresses
    
    def recurse(self, curr, ans, index, temp, count):
        # Base case 1: If we have formed more than 4 parts, it's invalid, so return from this recursive call.
        if count > 4:
            return

        # Base case 2: If we have formed exactly 4 parts and reached the end of the input string,
        # it means we have a valid IP address. So, append it to the 'ans' list.
        if count == 4 and index == len(curr):
            ans.append(temp)

        # Loop through different lengths for the current part (1 to 3 digits)
        for i in range(1, 4):
            # If the current part extends beyond the end of the input string, break out of the loop.
            if index + i > len(curr):
                break

            # Extract the current part from the input string.
            s = curr[index:index + i]

            # Check if the current part is invalid:
            # 1. If it starts with "0" and its length is greater than 1 (except for the part "0" itself).
            # 2. If the length is 3 and its integer value is greater than or equal to 256.
            if (s.startswith("0") and len(s) > 1) or (i == 3 and int(s) >= 256):
                continue  # Skip to the next iteration of the loop.

            # If the current part is valid, make a recursive call with updated parameters.
            # Append the current part to the 'temp' string and add a dot if 'count' is less than 3 (to separate parts).
            self.recurse(curr, ans, index + i, temp + s + ("." if count < 3 else ""), count + 1)

# Example usage
s = "25525511135"
sol = Solution()
print(sol.restoreIpAddresses(s))
