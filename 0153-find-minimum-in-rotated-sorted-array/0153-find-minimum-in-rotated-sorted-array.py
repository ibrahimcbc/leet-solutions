class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        if(len(nums)==2):
            return min(nums)
        while r>=l:
            mid=((l+r)//2)
            if nums[mid]>nums[0]:
                if nums[mid]>nums[-1]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[mid]==nums[-1]:
                    return nums[mid]
                elif nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                    return nums[mid]
                else:
                    r=mid
        return nums[r]