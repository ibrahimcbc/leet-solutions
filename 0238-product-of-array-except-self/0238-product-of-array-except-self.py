class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            answer= [1]*len(nums)
            multiplier=1
            for i in range(len(nums)):
                answer[i]*= multiplier
                multiplier*= nums[i]
            multiplier=1
            for k in range(len(nums)-1,-1,-1):
                answer[k]*= multiplier
                multiplier*= nums[k]
            return answer