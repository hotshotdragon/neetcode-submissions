class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        most_common = count.most_common(k)
        return [item[0] for item in most_common]