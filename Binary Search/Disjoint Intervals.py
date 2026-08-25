class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value):
        self.nums.add(value)

    def getIntervals(self):
        if not self.nums:
            return []

        nums = sorted(self.nums)
        intervals = []

        start = nums[0]
        end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                intervals.append([start, end])
                start = end = num

        intervals.append([start, end])
        return intervals
