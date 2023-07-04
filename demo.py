class Solution:
    
    def is_rotation(self, A:list, B:list)->bool:
        restructured_list = []
        is_printed = False
        for i in A:
            if len(B) != len (A):
                print("List A:\n{}".format(A))
                print("List B:\n{}".format(B))
                return "They are not restructured lists! :)"
            else:
                for i in A:
                    if i in B:
                        restructured_list.append(i)
                        if not is_printed:
                            print("They are restructured lists!")
                            is_printed = True
                return restructured_list
                    
sol = Solution()
A = [1,2,3,4,5,6,7]
B = [4,5,6,7,1,2,3]
result = sol.is_rotation(A,B)
print(result)

A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 8, 1, 2, 3]
result = sol.is_rotation(A,B)
print(result)
                    
