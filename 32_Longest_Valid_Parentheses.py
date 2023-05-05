def longest_parenthesis(s):
    #maintain the count of left as well as right parenthesis count
    l_count=r_count=max_len = 0
    
    #itrerate through the string
    i = 0
    while i<len(s):
        if s[i] == "(":        
            l_count += 1
        else:
            r_count += 1

        #if no, of open parenthesis is equal to close ones, find maximum sum(l+r)
        if l_count == r_count:
            max_len = max(max_len,l_count+r_count)

        #if closing parenthesis are more then, re-initialize both counts tp zero
        # helps in finding consecutive "()" pattern 
        elif r_count > l_count:
            l_count = r_count = 0

        i += 1

    #do same for checking string from back
    l_count = r_count = 0
    i = len(s)-1
    while i>=0:
        if s[i] == "(":
            l_count += 1
        else:
            r_count += 1

        if l_count == r_count:
            max_len = max(max_len,l_count+r_count)

        elif l_count > r_count:
            l_count = r_count = 0

        i -= 1

    return max_len

s = ")()()"
print(longest_parenthesis(s))