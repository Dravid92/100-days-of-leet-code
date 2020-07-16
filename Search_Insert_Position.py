class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        global fl
        for i in range(0,len(nums)):

            if target == nums[i] or target <= nums[i]:
                fl = i
                break
            elif target > nums[-1]:
                fl = len(nums)
                break
            elif target > nums[i] and target < nums[i+1]:
                fl = i+1
                break
                
        return fl



