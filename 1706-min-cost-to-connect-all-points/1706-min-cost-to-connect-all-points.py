class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0,0)]
        visited = [False]*n
        ans = 0
        count = 0

        while min_heap and count < n:
            wt, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            ans += wt
            count += 1
            for v in range(n):
                if not visited[v]:
                    x1, y1 = points[u]
                    x2, y2 = points[v]
                    new_wt = abs(x2 - x1) + abs(y2 - y1)
                    heapq.heappush(min_heap, (new_wt, v))

        return ans