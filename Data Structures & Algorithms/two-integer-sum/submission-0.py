class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for inx, i in enumerate(nums):
            left = target - i
            if left in rem:
                return [rem[left],inx]
            rem[i] = inx
        return []