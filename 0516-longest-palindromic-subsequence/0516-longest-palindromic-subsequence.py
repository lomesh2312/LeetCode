class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}

        def helper(s, a, b):
            if a == b:
                return 1
            if a>b:
                return 0 
            if (a,b) in dp:
                return dp[(a,b)]
            if s[a] == s[b]:
                dp[(a,b)] = 2 + helper(s,a+1,b-1)
            else:
                dp[(a,b)] = max(helper(s,a+1,b), helper(s,a,b-1))
            return dp[(a,b)]

        return helper(s,0,len(s)-1)

        