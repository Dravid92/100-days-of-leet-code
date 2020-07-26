"""

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)

        i = 0
        while i<=len(nums)-1:
            if nums[i] == val:
                nums.remove(nums[i])
                n = n -1
                i = i-1
            else:
                pass
            i = i+1
        else:
            n = n
            
        return n
        

"""

Runtime: 28 ms, faster than 93.13% of Python3 online submissions for Remove Element.
Memory Usage: 14 MB, less than 12.42% of Python3 online submissions for Remove Element.

"""