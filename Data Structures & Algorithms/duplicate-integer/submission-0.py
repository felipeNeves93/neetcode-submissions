class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        s = set()
        for n in nums:
            s.add(n)
        
        return len(s) < len(nums)
            