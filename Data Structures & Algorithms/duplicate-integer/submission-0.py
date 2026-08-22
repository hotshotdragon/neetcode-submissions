class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        look = {}
        for i in nums:
            if i in look:
                return True
            look[i] = 1
        return False