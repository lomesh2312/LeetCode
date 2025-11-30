class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = {}

        def back(x,y):
            if x >= n or y >= m:
                return float('inf')

            if x == n-1 and y == m-1:
                return max(1, 1 - dungeon[x][y])

            if (x,y) in dp:
                return dp[(x,y)]

            down = back(x+1, y)
            right = back(x, y+1)

            dp[(x,y)] = max(1, min(down, right) - dungeon[x][y])
            return dp[(x,y)]

        return back(0,0)