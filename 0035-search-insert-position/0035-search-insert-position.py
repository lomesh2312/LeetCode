class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        le = 0
        ri = len(nums) -1 
        while le <= ri:
            mid = (le+ri)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                le = mid + 1
            else:
                ri = mid - 1
        return le