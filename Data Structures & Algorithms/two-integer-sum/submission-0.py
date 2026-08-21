class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looks = {}
        for inx, num in enumerate(nums):
            val = target - num
            if val in looks:
                return [looks[val], inx] 
            looks[num] = inx
        return []