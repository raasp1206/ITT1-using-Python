class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        def merge_sort(left, right):
            if right - left <= 1:
                return 0
     
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            low = high = mid
            for left_val in prefix_sums[left:mid]:
                while low < right and prefix_sums[low] - left_val < lower:
                    low += 1
                while high < right and prefix_sums[high] - left_val <= upper:
                    high += 1
                count += high - low
                
            prefix_sums[left:right] = sorted(prefix_sums[left:right])
            return count

        return merge_sort(0, len(prefix_sums))
