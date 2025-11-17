class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        queue = deque()

        for i in range(len(adj)):
            if indegree[i] == 0:
                queue.append(i)

        ans = []
        while queue:
            u = queue.popleft()
            ans.append(u)

            for nei in adj[u]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(ans) == numCourses:
            return ans

        else:
            return []