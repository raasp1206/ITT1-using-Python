class Solution:
    def convert(self, s: str, numRows: int) -> str: 
        if numRows==1:
            return s
        row = 0
        step = 1
        t=['']*numRows
        for i in range(len(s)):
            t[row]+=s[i]
            if row==numRows-1:
                step=-1
            elif row==0:
                step=1
            row=row+step            
        return ''.join(t)
