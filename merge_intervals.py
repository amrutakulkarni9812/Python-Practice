'''
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge_intervals(self, intervals):
        # First sort the intervals by their first elements
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        print(sorted_intervals)
        # Create new intervals list
        merged_intervals = list()
        # If the first element of a list is greater than second element of the previous list, then append the list as is
        for interval in sorted_intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        print(merged_intervals)
        return merged_intervals

sol = Solution()
sol.merge_intervals([[1,6],[1,10],[15,18],[2,6]])


