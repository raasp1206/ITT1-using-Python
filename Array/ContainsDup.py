class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        buckets = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):
            bucket_id = num // width
            if num < 0:
                bucket_id -= 1

            # Same bucket
            if bucket_id in buckets:
                return True

            # Previous bucket
            if (bucket_id - 1 in buckets and
                abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True

            # Next bucket
            if (bucket_id + 1 in buckets and
                abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True

            buckets[bucket_id] = num

            # Remove elements outside the sliding window
            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_bucket = old // width
                if old < 0:
                    old_bucket -= 1
                del buckets[old_bucket]

        return False
