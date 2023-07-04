class Solution:
    def common_element(self, A:list, B:list):
        common_elements =[]
        for i in A:
            if i in B:
                common_elements.append(i)
        if common_elements:
            print("These are the common numbers:", common_elements)
            return common_elements
        else:
            return None

sol = Solution()
# Define the input lists
A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]

result = sol.common_element(A,B)
print(result)
