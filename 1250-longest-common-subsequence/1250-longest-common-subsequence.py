class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def helper(s1, s2, m, n):
            if n == 0 or m == 0:
                return 0 
            if (m,n) in dp:
                return dp[(m,n)]
            if s1[m-1] == s2[n-1]:
                dp[(m,n)] = 1 + helper(s1, s2, m-1, n-1)
            else:
                dp[(m,n)] = max(helper(s1, s2, m-1, n), helper(s1, s2, m, n-1))
            return dp[(m,n)]
        return helper(text1, text2, len(text1), len(text2))
        