from collections import Counter

class Solution:
    def minStickers(self, stickers, target):
        sticker_counts = [Counter(sticker) for sticker in stickers]
        memo = {"": 0}

        def dfs(remain):
            if remain in memo:
                return memo[remain]

            target_count = Counter(remain)
            ans = float('inf')

            for sticker in sticker_counts:
                # Optimization: skip stickers that don't contain
                # the first needed character
                if remain[0] not in sticker:
                    continue

                new_remain = ""

                for ch in target_count:
                    if target_count[ch] > sticker.get(ch, 0):
                        new_remain += ch * (target_count[ch] - sticker.get(ch, 0))

                temp = dfs(new_remain)
                if temp != -1:
                    ans = min(ans, temp + 1)

            memo[remain] = -1 if ans == float('inf') else ans
            return memo[remain]

        # Sort target so memoization is consistent
        return dfs("".join(sorted(target)))
