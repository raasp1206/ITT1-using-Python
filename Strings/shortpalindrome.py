class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return ""
            
        rev_s = s[::-1]
        
        combined = s + "#" + rev_s
        
        n = len(combined)
        lps = [0] * n
        
        for i in range(1, n):
            j = lps[i - 1]
            
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
                
            if combined[i] == combined[j]:
                j += 1
                
            lps[i] = j
            

        longest_palindrome_prefix_len = lps[-1]
        

        suffix_to_reverse = s[longest_palindrome_prefix_len:]
        return suffix_to_reverse[::-1] + s
