class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def back(idx):
            if idx == len(nums):
                res.append(curr[:])
                return

            
            
            curr.append(nums[idx])
            back(idx+1)
            curr.pop()
            back(idx+1)

        back(0)
        return res
