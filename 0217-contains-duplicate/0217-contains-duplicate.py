class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        detect= {}
        for i in range(len(nums)):
            if nums[i] in detect:
                return True
            detect[nums[i]]=i
        return False
        