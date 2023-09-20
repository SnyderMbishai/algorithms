class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals):
        # sort list
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            current_interval = intervals[i - 1]
            next_interval = intervals[i]

            if next_interval.start < current_interval.end:
                return False
        return True


if __name__ == "__main__":
    intervals = [Interval(0, 10), Interval(10, 20)]
    print(Solution().canAttendMeetings(intervals))
    intervals2 = [Interval(0, 30), Interval(10, 20)]
    print(Solution().canAttendMeetings(intervals2))
    intervals3 = [Interval(0, 30)]
    print(Solution().canAttendMeetings(intervals3))
