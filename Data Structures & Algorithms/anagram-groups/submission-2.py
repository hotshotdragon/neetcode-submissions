from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for string in strs:
            str_ana = sorted(string)
            str_ana = "".join(str_ana)
            ana[str_ana].append(string)
        return [i for i in ana.values()]        