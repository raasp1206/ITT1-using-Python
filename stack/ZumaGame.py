from collections import deque

class Solution(object):
    def findMinStep(self, board, hand):
        def remove_consecutive(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return remove_consecutive(s[:i] + s[j:])
                i = j
            return s
        hand = "".join(sorted(list(hand)))
        queue = deque([(board, hand, 0)])
        visited = set([(board, hand)])
        while queue:
            curr_board, curr_hand, steps = queue.popleft()
            if not curr_board:
                return steps  
            for i in range(len(curr_board) + 1):
                for j in range(len(curr_hand)):
                    if j > 0 and curr_hand[j] == curr_hand[j - 1]:
                        continue                        
                    ball = curr_hand[j]
                    is_worth_inserting = False
                    if i < len(curr_board) and curr_board[i] == ball:
                        is_worth_inserting = True
                    elif i > 0 and curr_board[i - 1] == ball:
                        is_worth_inserting = True
                    elif i > 0 and i < len(curr_board) and curr_board[i - 1] != curr_board[i]:
                        is_worth_inserting = True                        
                    if not is_worth_inserting:
                        continue 
                    new_board = curr_board[:i] + ball + curr_board[i:]
                    new_board = remove_consecutive(new_board)                  
                    new_hand = curr_hand[:j] + curr_hand[j + 1:]
                    state = (new_board, new_hand)
                    if state not in visited:
                        visited.add(state)
                        queue.append((new_board, new_hand, steps + 1))
        return -1
