class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        ans = 0
        for i in range(len(target)):
            if target[i] > prev:
                ans += target[i] - prev
            prev = target[i]
        return ans
        