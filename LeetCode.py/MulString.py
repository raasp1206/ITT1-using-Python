class Solution(object):
    def multiply(self, num1, num2):
        # Quick check for zero edge cases
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        # The result array can have at most m + n digits
        pos = [0] * (m + n)
        
        # Multiply from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                
                # Sum with the existing value in the target slot
                total = mul + pos[p2]
                
                # Update the current slot and carry over to the left slot
                pos[p2] = total % 10
                pos[p1] += total // 10
                
        # Convert array to string, skipping leading zeros
        result = []
        for digit in pos:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))
                
        return "".join(result)
