class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp_l = [-1] * (n+1)
        dp_l[0] = dp_l[1] = 1

        for i in range(2,n+1):
            dp_l[i] = dp_l[i-1] + dp_l[i-2]
        return dp_l[n]
