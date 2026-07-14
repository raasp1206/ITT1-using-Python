class Solution(object):
    def largestMultipleOfThree(self, digits):
        counts = [0] * 10
        total_sum = 0
        for d in digits:
            counts[d] += 1
            total_sum += d
        mod1_digits = [1, 4, 7]
        mod2_digits = [2, 5, 8]
        
        def remove_digits(mod_list, count_to_remove):
            removed = 0
            for d in mod_list:
                while counts[d] > 0 and removed < count_to_remove:
                    counts[d] -= 1
                    removed += 1
            return removed == count_to_remove
            
        remainder = total_sum % 3
        if remainder == 1:
            if not remove_digits(mod1_digits, 1):
                remove_digits(mod2_digits, 2)
        elif remainder == 2:
            if not remove_digits(mod2_digits, 1):
                remove_digits(mod1_digits, 2)
                
        result = []
        for d in xrange(9, -1, -1):
            result.append(str(d) * counts[d])
            
        final_str = "".join(result)
        
        if final_str and final_str[0] == '0':
            return "0"
            
        return final_str
