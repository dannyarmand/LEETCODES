from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # initializing variables candidate and count
        candidate = None #candidate will store the potential majority element
        count = 0 # count will keep track of how many times the candidate appears

        #Looping through each element num in the input list nums
        for num in nums:
            # checking if the count is zero, which means no potential majority element candidate yet
            if count == 0:
                #setting the current element num as the new candidate and initializing count
                candidate = num
                count = 1

            # if the current element num is the same as the candidate increment the count
            elif candidate == num:
                count +=1
            #if the current element num is different from the candidate decrement the count
            else:
                count -=1
        return candidate 
nums = [3,2]
sol = Solution()
print(sol.majorityElement(nums))

# nums = [2,2,1,1,1,2,2]
# sol = Solution()
# print(sol.majorityElement(nums))

# nums = ['a','b','b', 'd', 'c']
# sol = Solution()
# print(sol.majorityElement(nums))
