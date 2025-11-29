class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = {}

        def back(x,y):
            if x == n-1:
                return triangle[x][y]

            if (x,y) in dp:
                return dp[(x,y)]

            down = back(x+1, y)
            right_dia = back(x+1, y+1)

            dp[(x,y)] = triangle[x][y] + min(down , right_dia)
            return dp[(x,y)]

        return back(0,0)