class Solution(object):
    def oddEvenJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return n            
        def get_next_jumps(sorted_indices):
            next_jumps = [None] * n
            stack = []
            for i in sorted_indices:
                while stack and stack[-1] < i:
                    next_jumps[stack.pop()] = i
                stack.append(i)
            return next_jumps
        odd_sorted = sorted(range(n), key=lambda x: (arr[x], x))
        next_odd = get_next_jumps(odd_sorted)
        even_sorted = sorted(range(n), key=lambda x: (-arr[x], x))
        next_even = get_next_jumps(even_sorted)
        odd = [False] * n
        even = [False] * n
        odd[n - 1] = True
        even[n - 1] = True
        for i in xrange(n - 2, -1, -1):
            if next_odd[i] is not None:
                odd[i] = even[next_odd[i]]
            if next_even[i] is not None:
                even[i] = odd[next_even[i]]
        return sum(odd)
