class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def back(x,y):
            if x == 0 and y == 0:
                return 0 if obstacleGrid[0][0] == 1 else 1
            if x < 0 or y < 0:
                return 0 
            if obstacleGrid[x][y] == 1:
                return 0
            if (x,y) in memo:
                return memo[(x,y)]
            
            memo[(x,y)] = back(x-1,y) + back(x,y-1)
            return memo[(x,y)]

        return back(m-1,n-1)