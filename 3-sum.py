class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        lt_final = []
        s = set()
        # n = 0
        i=0
        while i < len(nums):
            n=i+1
            while n < len(nums)-1:
                t = n+1
                while t <= len(nums)-1:
                    lst = []
                    lst.extend([nums[i],nums[n],nums[t]])
                    t=t+1
                    if sum(lst) == 0:
                        srtd = tuple(sorted(lst))
                        if srtd not in s:
                            lt_final.append(lst)
                            s.add(srtd)
                n = n+1
            i=i+1

        return lt_final
        