class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_n = (n + 1) // 2
        even_n = n - odd_n
        odd_m = (m + 1) // 2
        even_m = m - odd_m
        
        return even_n * odd_m + odd_n * even_m
