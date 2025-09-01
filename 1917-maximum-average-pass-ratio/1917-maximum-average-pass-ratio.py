from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Define a function to compute the gain in pass ratio
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # Use a max heap where we store (-gain, p, t)
        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Assign each extra student to the class with the max gain
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute final average pass ratio
        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(classes)
