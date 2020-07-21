"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""



"""
Runtime: 108 ms, faster than 6.32% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.6 MB, less than 94.34% of Python3 online submissions for Merge Sorted Array.
"""


"""
Solution
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2    
        i=0
        while i<len(nums1)-1:
            j = i+1   
            while j < len(nums1):
            # print(m[i], m[i+1])
                if nums1[i] > nums1[j]:
                    temp = nums1[j]
                    nums1[j] = nums1[i]
                    nums1[i] = temp
                j=j+1
            i=i+1



