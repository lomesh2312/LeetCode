class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        
        def back(x,y):
            if x == 1 and y ==1:
                return 1
            if x<1 or y<1:
                return 0 

            if (x,y) in dp:
                return dp[(x,y)]

            dp[(x,y)] = back(x-1,y) + back(x,y-1)
            return dp[(x,y)]

        return back(m,n)