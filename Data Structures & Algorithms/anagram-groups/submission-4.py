from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for string in strs:
            # Inline the sorting and joining
            ana["".join(sorted(string))].append(string)
        
        # list() is slightly faster and cleaner than list comprehension
        return list(ana.values())