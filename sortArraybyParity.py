from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        answer = []

        #we split nums into even entries and odd entries
        even = [n for n in nums if n%2 == 0]
        odd = [n for n in nums if n%2 ==1]

        #we fill the answer wit even and odd entries
        for a,b in zip(even, odd):
            answer.append(a)
            answer.append(b)
    
        return answer

sol = Solution()
nums1 = [3,4,5,9,11,22,36,176,0,24]
result = sol.sortArrayByParityII(nums1) 
print(result)            
