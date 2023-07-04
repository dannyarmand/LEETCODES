class Solution:
    def most_frequent(self, given_list):
        # Check if the given list is empty
        if len(given_list) == 0:
            return None  # If the list is empty, return None

        # Create an empty dictionary to store item counts
        counts = {}

        # Iterate over each item in the given list
        for item in given_list:
            # If the item is already in the dictionary, increment its count by 1
            if item in counts:
                counts[item] += 1
            # If the item is not in the dictionary, add it with a count of 1
            else:
                counts[item] = 1

        # Initialize variables to keep track of the maximum count and the item with the maximum count
        max_count = 0
        max_item = None

        # Iterate over each item and its count in the dictionary
        for item, count in counts.items():
            # If the current count is greater than the maximum count,
            # update the maximum count and the item with the maximum count
            if count > max_count:
                max_count = count
                max_item = item

        # Return the item with the maximum count
        return max_item
