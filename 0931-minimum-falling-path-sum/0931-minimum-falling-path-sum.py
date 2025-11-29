class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = {}

        def back(x,y):
            if y >= n or y < 0:
                return float('inf')

            if x == n-1:
                return matrix[x][y]

            if (x,y) in dp:
                return dp[(x,y)]

            down = back(x+1, y)
            left_dia = back(x+1, y+1)
            right_dia = back(x+1, y-1)

            dp[(x,y)] = matrix[x][y] + min(down, left_dia, right_dia)
            return dp[(x,y)]

        ans = float('inf')
        for j in range(n):
            ans = min(ans, back(0,j))
        
        return ans