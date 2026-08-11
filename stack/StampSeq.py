class Solution(object):
    def movesToStamp(self, stamp, target):
        M, N = len(stamp), len(target)
        target_list = list(target)
        final_target = ['?'] * N
        res = []
        def can_match(i):
            matched = False
            for j in range(M):
                if target_list[i + j] == stamp[j]:
                    matched = True  
                elif target_list[i + j] == '?':
                    continue
                else:
                    return False
            return matched
        def do_stamp(i):
            for j in range(M):
                target_list[i + j] = '?'
        changed = True
        while changed:
            changed = False
            for i in range(N - M + 1):
                if can_match(i):
                    do_stamp(i)
                    res.append(i)
                    changed = True
                    if target_list == final_target:
                        break
            
            if target_list == final_target:
                break
        if target_list != final_target:
            return []
        return res[::-1]
