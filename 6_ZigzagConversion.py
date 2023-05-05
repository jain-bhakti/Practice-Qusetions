def convert(s,numRows):
    if numRows == 1:          #if print in 1 row return the original string itself
        return s

    res = ""
    for r in range(numRows):
        increment = 2*(numRows-1)            #increment tells about the each next character row-wise after a fixed interval
        for i in range(r,len(s),increment):
            res += s[i]                      #works for first and the last row 

            if r>0 and r<numRows-1 and i+increment-2*r < len(s):   #for middle rows
                res += s[i+increment-2*r]                       # append the letter located in between the fully filled columns

    return res

s = "PAYPALISHIRING"
numRows = 3
print(convert(s,numRows))