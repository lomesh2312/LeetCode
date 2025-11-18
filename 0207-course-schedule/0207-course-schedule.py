class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(ans) == numCourses:
            return True
        else:
            return False