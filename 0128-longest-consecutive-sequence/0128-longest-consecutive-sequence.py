class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        num_set = set(nums)
        max_count = 1
        temp_count = 1
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                while current_num + 1 in num_set:
                    current_num += 1
                    temp_count += 1
                max_count = max(max_count, temp_count)
                temp_count = 1
                
        return max_count





