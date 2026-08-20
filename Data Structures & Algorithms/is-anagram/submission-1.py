class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = t.replace(" ", "").lower()
        s2 = s.replace(" ", "").lower()
        return sorted(s1) == sorted(s2)