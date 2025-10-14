class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def end_sort(interval):
            return interval[1]

        def helper(nums):
            nums.sort(key = end_sort)
            last = nums[0][1]
            ans = 0

            for i in range(1, len(nums)):
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]

                if last > curr_start:
                    ans += 1
                else:
                    last = curr_end
            return ans
        return helper(intervals)

        